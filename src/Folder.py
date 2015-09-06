import os
import yaml
import TypeManager

class File:
	def __init__(self, path, typeManager):
		self._path = path
		self._type = typeManager.fileToItem(path)

class Folder:
	def __init__(self, rootPath, typeManager):
		self._rootPath = rootPath
		self._folders = {}
		self._tm = typeManager

	def analyse(self):
		self._files = []
		# Recursive analysis
		for f in os.listdir(self._rootPath):
			path = os.path.join(self._rootPath, f)
			if not os.path.isfile(path):
				folder = Folder(path, self._tm)
				folder.analyse()
				self._folders[path] = folder
			else:
				fil = File(path, self._tm)
				self._files.append(fil)
		# Actual analysis
		self._type = self._tm.guess(self._files, self._folders)
		return self._type

	def print(self):
		print(self._folders)

	def generateDef(self):
		d = {self._rootPath: {'type':self._type._name, 'files': {}, 'folders': {}}}
		files = d[self._rootPath]['files']
		folders = d[self._rootPath]['folders']
		for f in self._files:
			files[f._path] = f._type._name
		for fo in self._folders:
			folders[self._folders[fo]._rootPath] = self._folders[fo]._type._name
		for fo in self._folders:
			d = dict(list(d.items()) + list(self._folders[fo].generateDef().items()))
		return d

	def saveToYaml(self, out):
		d = self.generateDef()
		open(out, 'w').write(yaml.dump(d, default_flow_style=False))
