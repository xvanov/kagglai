# general
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import numpy as np

# validation
from sklearn.model_selection import cross_validate

# modleing
from sklearn.ensemble import RandomForestClassifier

# bayesian optimization
from skopt import BayesSearchCV

# genetic algorithm optimization
from pygad import GA

# custom
import src.custom_exceptions

class Tuner():

    def __init__(self, model, x, y, params=None):
        self.model = model
        self.x = x
        self.y = y
        self.modelName = type(model).__name__
        self.choose_model_params(self.modelName)
        self.params = params
        global X
        global Y
        global CV
        X = self.x
        Y = self.y
        CV = self.cv


    def choose_model_params(self, modelType):
        if modelType == 'RandomForestClassifier':
            self.space = {
                         'n_estimators':(10, 500),
                         'max_depth':(10, 100),
                         'min_samples_leaf':(1, 100),
                         'min_samples_split':(2, 25),
                         'max_features':['auto', 'sqrt', 'log2'] }
            self.cv = 3
            self.n_iter = 32

    def tune(self, optMethod):
        if optMethod==None:
            optMethod = self.optMethod

        if optMethod == 'bayes':
            opt = self.bayes_opt()
        elif optMethod == 'genetic':
            opt = self.genetic_opt(self.params)
        else:
            opt = None
            raise custom_exceptions.InvalidTuningMethod(optMethod)
        return opt

    def bayes_opt(self):
        opt = BayesSearchCV(self.model,
                            self.space,
                            n_iter=self.n_iter,
                            cv=self.cv)
        print(self.x)
        print(self.y)
        print(type(self.x))
        print(type(self.y))
        print(self.space)
        opt.fit(self.x, self.y)
        return opt

    def genetic_opt(self, params=None):
        fitnessFunc, geneSpace = self.choose_fitness(self.modelName)
        if params==None:
            cardinality = len(geneSpace)
            params = self.choose_genetic_params(cardinality)
        opt = GA(fitness_func=fitnessFunc,
                 gene_space=geneSpace,
                 **params)
        opt.run()
        return opt

    def choose_genetic_params(self, cardinality):

        if self.modelName == 'RandomForestClassifier':
            params = {
                'sol_per_pop':4,
                'num_genes':cardinality,
                'num_generations':10,
                'num_parents_mating':3,
                'parent_selection_type':"sss",
                'keep_parents':1,
                'crossover_type':"single_point",
                'mutation_type':"random",
                'mutation_percent_genes':20}
        return params


    def choose_fitness(self, modelName):
        if modelName == 'RandomForestClassifier':
            fitnessFunc = random_forest_fitness
            geneSpace = []
        for k in self.space:
            s = self.space[k]
            stype = type(s[0])
            if stype==int:
                geneSpace.append(s)
        return fitnessFunc, geneSpace

def random_forest_fitness(solution, solution_idx):
    # TODO: integrate genetic opt with common bayes optimization api
    rfc = RandomForestClassifier(n_estimators=int(solution[0]),
                                 max_depth=int(solution[1]),
                                 min_samples_leaf=int(solution[2]),
                                 min_samples_split=int(solution[3]),
                                oob_score=True)
    oobScores = []
    for i in range(CV):
        rfc.fit(X, Y)
        oobScores.append(rfc.oob_score_)
    fitness = np.mean(oobScores)
    return fitness

if __name__ == "__main__":
    pass
