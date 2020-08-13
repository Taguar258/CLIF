from CLIF_Framework.framework import event
event = event()

class Temp:
   def __init__(selfie, console):
      global self
      global var
      self = selfie
      var = console
      
      self._main()
   
   def _main(self):
      # Put your event help, etc. in here.
      pass

def setup(console):
   console.add(Temp(console), event)
