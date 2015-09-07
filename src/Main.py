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

# Folder Analysis
folderAnalysis = FolderAnalyser.analyseFolder(rootDir)
YamlWriter.saveToYaml(folderAnalysis, faOut)
print('Folder Analysis saved to ' + faOut)

# List generator
listOutput = ListGenerator.generateList(folderAnalysis)
YamlWriter.saveToYaml(listOutput, loOut)
print('Generated List saved to ' + loOut)





