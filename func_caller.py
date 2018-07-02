import callee

def callback():
  return 'call back in func_caller'

def call():
  callee.func()

call()
