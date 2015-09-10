import TypeManager

def choose(allEl, choice, ma):
	split = choice.split(' ')
	# Choice like "first filename" or "last size"
	if len(split) == 2:
		field = split[-1]
		first = split[-2] == 'first'
		if field == 'filename':
			ordered = sorted([p.split('/')[-1] for p in allEl.keys()])
		else:
			ordered = []
			for k, v in allEl.items():
				index = 1
				while index < len(ordered) and ordered[index-1] > v[field]:
					index = index + 1
				ordered.insert(index - 1, k)
		return ordered[:ma]

def getElements(folder, r):
	allEl = getAllElements(folder, r)
	if r['max'] == 0 or len(allEl.keys()) <= r['max']:
		return list(allEl.keys())
	if len(allEl.keys()) < r['min']:
		return []
	# Here, we know that we have too much matching elements
	ret = choose(allEl, r['choice'], r['max'])
	# Ordering
	# ...
	return ret

	
def getAllElements(folder, r):
	ret = {}
	rType = r['type'].split('/')[-1]
	for fPath, f in list(folder['files'].items()) + list(folder['folders'].items()):
		if f['type'] == rType:
			ret[fPath] = f
	return ret

def getRemainings(allF, listed):
	ret = []
	for f in allF:
		if not f in listed:
			ret.append(f)
	return ret

def generateList(fa, tm):
	output = {}
	for kf, f in fa.items():
		# Create element
		typ = tm.getSet(f['type'])
		el = {}
		
		# Required
		for kr, r in [] if typ is None else typ._required.items():
			el[kr] = getElements(f, r)
		# Optional
		for ko, o in [] if typ is None else typ._optional.items():
			el[ko] = getElements(f, o)
		# Other files
		allFilesAndFolders = list(f['files'].keys()) + list(f['folders'].keys())
		listedFilesAndFolders = []
		for elval in el.values():
			listedFilesAndFolders.extend([] if elval is None else elval)
		el['otherFiles'] = getRemainings(allFilesAndFolders, listedFilesAndFolders)
		# Add element to output
		output.setdefault('unkown' if typ is None else typ._name, {})
		output['unkown' if typ is None else typ._name][kf] = el
	return output
