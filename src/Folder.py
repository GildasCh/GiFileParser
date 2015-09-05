import os
import TypeManager

class Folder:
	def __init__(self, rootPath, itemsPath, setsPath):
		self._rootPath = rootPath
		self._folders = {}
		self._tm = TypeManager.TypeManager(itemsPath, setsPath)

	def analyse(self):
		self.analyseDir(self._rootPath)

	def analyseDir(self, path):
		files = []
		sets = []
		# Recursive analysis
		for f in os.listdir(path):
			if not os.path.isfile(os.path.join(path, f)):
				sets.append(self.analyseDir(os.path.join(path,f)))
			else:
				files.append(f)
		# Actual analysis
		t = self._tm.guess(files, sets)
		self._folders[path] = t
		return t

	def print(self):
		print(self._folders)
