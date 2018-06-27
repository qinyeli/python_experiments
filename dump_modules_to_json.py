import utils
import modules.moduleA as moduleA
from modules.moduleB import moduleB

imported_modules = utils.imported_modules(globals())

def _write_modules_to_json(modules, json_file):
  import json
  with open(json_file, 'w') as f:
    json.dump(modules, f)

_write_modules_to_json(imported_modules, 'modules.json')

print('These module infos are dumped to modules.json:')
print(imported_modules)
