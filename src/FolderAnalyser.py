import sys
sys.path.append('src')
import Folder
import TypeManager

itemsDir = 'config/items'
setsDir = 'config/sets'

def analyseFolder(path):
	tm = TypeManager.TypeManager(itemsDir, setsDir)
	f = Folder.Folder(path, tm)
	f.analyse()
	return f.generateDef()
