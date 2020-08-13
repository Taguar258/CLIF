Mastering the CLIF framework
--------------------------------------------------
We will now start creating our first interface using CLIF, it is going to be a menu eventough CLIF is not directly made for menus and can make very simple menus complex, but it's a good example and perfect for complex ones.

**At the beginning of any project you will need to download the CLIF folder and rename it to any project name you want.**

We will then start a new project.
If you have a look inside your project's folder you will be able to see two folders and one file.
The folder "CLIF-Framework" is basically the source code for the framework but in most cases you will not needed to modify it.
The other folder called modules can be used to store your source code for the interface.

If you open the file "main.py" you will see this:
```
import CLIF-Framework.framework as framework
 
console = framework.console()
 
framework.module("modules.main", console)
 
console.run()
```

The line  `import CLIF-Framework.framework as framework` basically imports the framework it self.
After that, the line `console = framework.console()` sets the variable `console` to the console class which means that the variable `console` defines a new interface.
The line `framework.module("modules.main", console)` loads your script located under modules/main as a interpreter for the variable `console`.
The last line `console.run()` tells the interface `console` to start.
The main file basically calls the first console/interface which basically loads your script as the logic of the interface.
It is a bit complicated at first but should be clear later on.

You can just keep the file as is and have a view at the file modules/main.py:
```
from CLIF-Framework.framework import event
event = event()

class Temp:
   def __init__(selfie, console):
      global self
      global var
      self = selfie
      var = console
      
      self._main()
   
   def main(self):
      # Put your event help, etc. in here.
      pass

def setup(console):
   console.add(Temp(console), event)
```

Here you can see the basic structure of a "module".
