import pandas as pd

from sklearn.model_selection import train_test_split

from src.dirtools import Dirs

class PP():
    def __init__(self, dirs):
        self.dirs = dirs


    def split_save(self, rawDataframe, yName, randomSeed=0, save=True):
        x = rawDataframe.drop(yName, axis=1)
        y = rawDataframe[yName]
        train_x, test_x, train_y, test_y = train_test_split(x, y, random_state = randomSeed)
        test_y.to_frame().reset_index().to_feather(self.dirs.Y_TST_PATH)
        train_y.to_frame().reset_index().to_feather(self.dirs.Y_TRN_PATH)

        test_x.reset_index().to_feather(self.dirs.X_TST_PATH)
        train_x.reset_index().to_feather(self.dirs.X_TRN_PATH)
