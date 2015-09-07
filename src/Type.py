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
		if 'terminal' in self._def:
			self._terminal = self._def['terminal']
		else:
			self._terminal = False
		# Defaults (diff. for required and optional)
		for vr in list(self._required.values()):
			if not 'min' in vr:
				vr['min'] = 1
		for vo in list(self._optional.values()):
			if not 'min' in vo:
				vr['min'] = 0
		# Common defaults
		for val in list(self._required.values()) + list(self._optional.values()):
			if not 'max' in val:
				val['max'] = 1
			if not 'choice' in val:
				val['choice'] = 'first filename'
			if not 'order' in val:
				val['order'] = 'filename'
			if not 'weight' in val:
				val['weight'] = 1
			if not 'standalone' in val:
				val['standalone'] = False
		

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
		
	def matchArrays(self, fa, sa):
		score = 0
		for si in sa:
			split = si['type'].split('/')
			m = split[-2]
			t = split[-1]
			matches = 0
			while t in fa and (si['max'] == 0 or matches < si['max']):
				matches = matches + 1
				fa.remove(t)
				score = score + si['weight']
		return score
				
	def matchScore(self, files, folders):
		score = 0
		ret = {'type': self._name}
		for tdef in [self._required[kr]['type'] for kr in self._required]:
			if not self.isThere(files, folders, tdef):
				return 0
			# Score
		folderArray = [f._type for f in files]
		folderArray.extend([folders[f]._type for f in folders])
		setArray = [self._required[t] for t in self._required]
		setArray.extend([self._optional[t] for t in self._optional])
		return self.matchArrays(folderArray, setArray)
		


	
