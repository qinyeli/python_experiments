import callee

def callback():
  return 'call back in obj_call'

def call():
  callee.func()

call()
