import os
import sys
import yaml
sys.path.append('src')
import folderAnalyser

def analyse(rootdir):
        for dir in [d for d in os.listdir(rootdir) if not os.path.isfile(os.path.join(rootdir,d))]:
                terminal, movie = fa.analyse(os.path.join(rootdir,dir))
                print(movie)
                if not terminal:
                        analyse(os.path.join(rootdir,dir))

# Main

rootdir = sys.argv[1]

fs = yaml.load(open('config/folderStructs/movie/folder.yml'))
fa = folderAnalyser.FolderAnalyser(fs)

analyse(rootdir)




