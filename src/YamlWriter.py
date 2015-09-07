import yaml

def saveToYaml(d, out):
	open(out, 'w').write(yaml.dump(d, default_flow_style=False))
