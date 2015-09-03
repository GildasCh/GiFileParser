import os

class FolderAnalyser:
	def __init__(self, folderStruct):
		self._fs = FolderStruct(folderStruct)
	
	def analyse(self, folder):
		return self._fs.comply(folder)

class FolderStruct:
	def __init__(self, yamlDef):
		self._required = yamlDef['folder']['required']
		self._optional = yamlDef['folder']['optional']
		self._terminal = yamlDef['folder']['terminal']
		# print(yamlDef)
		# print(self._required)
		
	def comply(self, folder):
		files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder,f))]
		ret = {}

		# Required files
		for kr in self._required:
			found = False
			for f in files:
				fname, ext = os.path.splitext(f)
				if ext in self._required[kr]:
					ret[kr] = os.path.abspath(os.path.join(folder,f))
					found = True
					break
			if not found:
				return False, None

		# Optional files
		for ko in self._optional:
			found = False
			for f in files:
				fname, ext = os.path.splitext(f)
				if ext in self._optional[ko]:
					ret[ko] = os.path.abspath(os.path.join(folder,f))
					found = True
					break
			
		return self._terminal, ret
