def imported_modules(globals_dict):
  def _yield_all_modules():
    import types
    for alias, module in globals_dict.items():
      if isinstance(module, types.ModuleType):
        if alias is not '__builtins__':
          yield (alias, module.__name__)
  return dict(_yield_all_modules())
