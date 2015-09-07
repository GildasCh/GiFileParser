import TypeManager

def getElements(folder, r):
	ret = []
	rType = r['type'].split('/')[-1]
	for fPath, f in list(folder['files'].items()) + list(folder['folders'].items()):
		if f['type'] == rType:
			ret.append(fPath)
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
		for kr, r in typ._required.items():
			el[kr] = getElements(f, r)
		# Optional
		for ko, o in typ._optional.items():
			el[ko] = getElements(f, o)
		# Other files
		allFilesAndFolders = list(f['files'].keys()) + list(f['folders'].keys())
		listedFilesAndFolders = []
		for elval in el.values():
			listedFilesAndFolders.extend(elval)
		el['otherFiles'] = getRemainings(allFilesAndFolders, listedFilesAndFolders)
		# Add element to output
		output.setdefault(kf, [])
		output[kf].append(el)
	return output
