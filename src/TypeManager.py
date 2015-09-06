import os
import yaml
import Type


class TypeManager:
	def __init__(self, itemsPath, setsPath):
		# Items
		self._items = []
		for i in os.listdir(itemsPath):
			if not os.path.isfile(os.path.join(itemsPath, i)) \
			   or i.endswith('~'):
				continue
			name, ext = os.path.splitext(i)
			ydef = yaml.load(open(os.path.join(itemsPath, i)))
			for k in ydef:
				self._items.append(Type.Item(k, ydef[k]))
		# Sets
		self._sets = []
		for s in os.listdir(setsPath):
			if not os.path.isfile(os.path.join(setsPath, s)) \
			   or i.endswith('~'):
				continue
			name, ext = os.path.splitext(s)
			ydef = yaml.load(open(os.path.join(setsPath, s)))
			for k in ydef:
				self._sets.append(Type.Set(k, ydef[k]))
		# Data
		self._data = []

	def fileToItem(self, f):
		for i in self._items:
			if i.match(f):
				return i
		
	def guess(self, files, folders):
		# Guess set
		ret = Type.Type('unkown')
		bestScore = 0
		for s in self._sets:
			score = s.matchScore(files, folders)
			if score > bestScore:
				bestScore = score
				ret = s
		return ret


				
