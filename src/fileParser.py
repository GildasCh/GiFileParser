import os
import sys
import yaml
sys.path.append('src')
import folderAnalyser

rootdir = sys.argv[1]

fs = yaml.load(open('config/folderStructs/movie/folder.yml'))
fa = folderAnalyser.FolderAnalyser(fs)

for root, subFolders, files in os.walk(rootdir):
	ret, movie = fa.analyse(root)
	if ret:
		print(movie)

