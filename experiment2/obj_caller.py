import callee

class Caller(object):
  def callback(self):
    return 'callback in obj_caller'
  
  def call(self):
    callee.func()

caller = Caller()
caller.call()
