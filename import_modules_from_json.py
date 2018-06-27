import utils

def _read_modules_from_json(json_file):
  import json
  with open(json_file, 'r') as f:
    return json.load(f)

modules_to_import = _read_modules_from_json('modules.json')

def _import_modules(modules):
  import importlib
  for alias, module_name in modules.items():
    globals()[str(alias)] = importlib.import_module(str(module_name))

_import_modules(modules_to_import)

print('The following modules are succesfully imported:')
imported_modules = utils.imported_modules(globals())
print(imported_modules)

# Make sure moduleA and moduleB are imported
print('\nCalling functions to check the modules are successfully imported')
print(moduleA.funcA())
print(moduleB.funcB())

