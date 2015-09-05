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

	def isThere(self, items, sets, tdef):
		split = tdef.split('/')
		m = split[-2]
		t = split[-1]
		if m == 'i':
			return t in items
		else:
			return t in sets
		
	def matchScore(self, items, sets):
		score = 0
		for kr in self._required:
			tdef = self._required[kr]
			if not self.isThere(items, sets, tdef):
				return 0
			score = score + 1
		for ko in self._optional:
			tdef = self._optional[ko]
			if self.isThere(items, sets, tdef):
				score = score + 1
		return score
		
