import sys
import yaml
sys.path.append('ext')
import Rx

# data = yaml.load(open("foo.yaml"))

rx = Rx.Factory({ "register_core_types": True })
schema = rx.make_schema(yaml.load(open("config/types/movie.yml")))

if not schema.check(data):
	raise ValueError("data file contents are not in a valid format")
