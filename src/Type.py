import yaml
import os

class Type:
	def __init__(self, name):
		self._name = name

	def __eq__(self, other):
		if isinstance(other, str):
			return self._name == other
		return NotImplemented

	def __str__(self):
		return self._name
	
	def __repr__(self):
		return self._name
	
class Item(Type):
	def __init__(self, name, definition):
		# super(Type, self).__init__(name)
		self._name = name
		self._def = definition

	def match(self, filename):
		fn, ext = os.path.splitext(filename)
		return ext in self._def
		
class Set(Type):
	def __init__(self, name, definition):
		# super(Type, self).__init__(name)
		self._name = name
		self._def = definition
		if 'required' in self._def:
			self._required = self._def['required']
		else:
			self._required = {}
		if 'optional' in self._def:
			self._optional = self._def['optional']
		else:
			self._optional = {}

	def isThere(self, files, folders, tdef):
		split = tdef.split('/')
		m = split[-2]
		t = split[-1]
		if m == 'i':
			for f in files:
				if t == f._type:
					return True
			return False
		else:
			for fo in folders:
				if t == folders[fo]._type:
					return True
			return False
		
	def find(self, items, sets, tdef):
		split = tdef.split('/')
		m = split[-2]
		t = split[-1]
		if m == 'i':
			for i in items:
				if t == i:
					return items[i]
		else:
			for s in sets:
				if t == s:
					return s

	def matchArrays(self, fa, sa):
		matchArray = []
		for si in sa:
			split = si.split('/')
			m = split[-2]
			t = split[-1]
			if t in fa:
				matchArray.append(t)
				fa.remove(t)
				# Array
				if len(split) >= 3 and split[-3] == 'a':
					while t in fa:
						matchArray.append(t)
						fa.remove(t)
		return len(matchArray)
				
	def matchScore(self, files, folders):
		score = 0
		ret = {'type': self._name}
		for kr in self._required:
			tdef = self._required[kr]
			if not self.isThere(files, folders, tdef):
				return 0
				#ret[kr] = self.find(items, sets, tdef)
			# Score
		folderArray = [f._type for f in files]
		folderArray.extend([folders[f]._type for f in folders])
		setArray = [self._required[t] for t in self._required]
		setArray.extend([self._optional[t] for t in self._optional])
		return self.matchArrays(folderArray, setArray)
		


	
