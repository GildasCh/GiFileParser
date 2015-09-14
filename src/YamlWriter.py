import yaml

def saveToYaml(d, out):
	with open(out, 'w') as fp:
		yaml.dump(d,
				  stream=fp,
				  default_flow_style=False,
				  default_style='\'',
				  allow_unicode=True)

	#f = open(out,"wb")
	#f.write(yaml.dump(d,
	#				  allow_unicode=True,encoding="utf-8"))

def openYaml(inp):
	return yaml.load(open(inp, 'r'))
