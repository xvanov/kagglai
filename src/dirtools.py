import os


class Dirs():
    def __init__(self, basePath, srcPath, dataPath,
                 projectName, trainPath='train.csv', testPath='test.csv',
                 samplePath='sample_submission.csv',
                 descriptionPath='data_description.csv'):
        self.BASE_DIRECTORY = os.path.dirname(basePath)
        self.CODE_DIRECTORY = os.path.join(self.BASE_DIRECTORY, srcPath)
        self.DATA_DIRECTORY = os.path.join(self.BASE_DIRECTORY, dataPath)

        self.PROJECT_DIRECTORY = os.path.join(self.DATA_DIRECTORY, projectName)
        self.IN_DIRECTORY = os.path.join(self.PROJECT_DIRECTORY, 'in')
        self.OUT_DIRECTORY = os.path.join(self.PROJECT_DIRECTORY, 'out')
        self.RAW_TRAIN_PATH = os.path.join(self.IN_DIRECTORY, trainPath)
        self.RAW_TEST_PATH = os.path.join(self.IN_DIRECTORY, testPath)
        self.RAW_SAMPLE_PATH = os.path.join(self.IN_DIRECTORY, samplePath)

        self.X_TST_PATH = os.path.join(self.IN_DIRECTORY, 'x_tst.feather')
        self.X_TRN_PATH = os.path.join(self.IN_DIRECTORY, 'x_trn.feather')
        self.Y_TST_PATH = os.path.join(self.IN_DIRECTORY, 'y_tst.feather')
        self.Y_TRN_PATH = os.path.join(self.IN_DIRECTORY, 'y_trn.feather')

