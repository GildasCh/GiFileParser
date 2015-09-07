import sys
sys.path.append('src')
import Folder

def analyseFolder(path, tm):
	f = Folder.Folder(path, tm)
	f.analyse()
	return f.generateDef()
