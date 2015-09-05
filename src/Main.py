import os
import sys
import yaml
sys.path.append('src')
import Folder

# Main

rootDir = sys.argv[1]
itemsDir = 'config/items'
setsDir = 'config/sets'

f = Folder.Folder(rootDir, itemsDir, setsDir)
f.analyse()
f.print()




