import os
import sys
import yaml
sys.path.append('src')
import Folder
import TypeManager

# Main

rootDir = sys.argv[1]
outFile = sys.argv[2]
itemsDir = 'config/items'
setsDir = 'config/sets'
outputDIr = 'output'

f = Folder.Folder(rootDir, TypeManager.TypeManager(itemsDir, setsDir))
f.analyse()
f.print()

f.saveToYaml(outFile)
print('Output saved to ' + outFile)




