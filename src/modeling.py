from src.dirtools import Dirs

class Modeler():
    def __init__(self, dirs):
        pass

if __name__=='__main__':
    basePath = ''
    srcPath = ''
    dataPath = ''
    projectName = 'testing'
    dirs = Dirs(basePath, srcPath, dataPath, projectName)
    m = Modeler(dirs)
