# pytest utils
import os,sys,inspect
import pytest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

# data
import pandas as pd
import numpy as np
# modeling
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# to test
from src.tuning import *
from src.custom_exceptions import *

# prepare data
data = load_iris()
x = pd.DataFrame(data['data'],columns=data['feature_names'])
y = data['target']
xtrn, xtst, ytrn, ytst = train_test_split(x,y,test_size=0.2)
xtrn = xtrn.to_numpy()

# make tests

def test_init_tuner():
    rfc = RandomForestClassifier()
    t = Tuner(rfc, xtrn, ytrn)
    assert t.modelName =='RandomForestClassifier'


def test_bayes():
    rfc = RandomForestClassifier()
    t = Tuner(rfc, xtrn, ytrn)
    t.cv = 3
    t.n_iter = 4
    opt = t.tune('bayes')

def test_genetic():
    rfc = RandomForestClassifier()
    t = Tuner(rfc, xtrn, ytrn)
    t.cv = 3
    t.n_iter = 4
    t.params = {
                'sol_per_pop':3,
                'num_genes':4,
                'num_generations':3,
                'num_parents_mating':2,
                'parent_selection_type':"sss",
                'keep_parents':1,
                'crossover_type':"single_point",
                'mutation_type':"random",
                'mutation_percent_genes':20}
    t.tune('genetic')


