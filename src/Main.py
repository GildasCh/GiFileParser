import sys
sys.path.append('src')
import Folder
import TypeManager
import FolderAnalyser
import ListGenerator
import YamlWriter

# Main

rootDir = sys.argv[1]
faOut = sys.argv[2]
loOut = sys.argv[3]
itemsDir = 'config/items'
setsDir = 'config/sets'

# Type Manager
tm = TypeManager.TypeManager(itemsDir, setsDir)

# Folder Analysis
folderAnalysis = FolderAnalyser.analyseFolder(rootDir, tm)
YamlWriter.saveToYaml(folderAnalysis, faOut)
print('Folder Analysis saved to ' + faOut)

# List generator
listOutput = ListGenerator.generateList(folderAnalysis, tm)
YamlWriter.saveToYaml(listOutput, loOut)
print('Generated List saved to ' + loOut)





