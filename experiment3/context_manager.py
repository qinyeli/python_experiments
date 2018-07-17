class ContextManager(object):
  def __init__(self):
    print('init')

  def __del__(self):
    print('del')

  def __enter__(self):
    print('>>> enter')
    return self  # This is passed to cm.

  def __exit__(self, exc_type, exc_val, exc_tb):
    print('<<< exit')

  def func(self):
    print('func')

with ContextManager() as cm:
  cm.func()
