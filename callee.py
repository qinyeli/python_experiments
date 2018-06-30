import sys

def func():
  print('>>> Enter func in callee >>>')

  import inspect
  caller_locals = inspect.currentframe().f_back.f_locals
  if 'self' in caller_locals:
    caller = caller_locals['self']
    print('Caller is an instance of %s.' % caller)
    callback = caller.callback
  else:
    print('Caller is not an object.')
    caller_globals = inspect.currentframe().f_back.f_globals
    callback = caller_globals['callback']
  print(callback())

  print('<<< Exit func in callee <<<')
