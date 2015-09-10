import yaml

def saveToYaml(d, out):
	open(out, 'w').write(yaml.dump(d,
								   default_flow_style=False,
								   default_style='\''))

def openYaml(inp):
	return yaml.load(open(inp, 'r'))
