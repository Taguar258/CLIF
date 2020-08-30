Mastering the CLIF framework
--------------------------------------------------
We will now start creating our first interface using CLIF, it is going to be a menu even tough CLIF is not directly made for menus and can make very simple menus complex, but it's a good example and perfect for complex ones.

**At the beginning of any project, you will need to <a href="https://github.com/Taguar258/CLIF/releases/download/1.0/CLIF-Clean.zip">download the CLIF Template</a> and rename it to any project name you want.**

We will then start a new project.
If you have a look inside your project's folder you will be able to see two folders and one file.
The folder "CLIF-Framework" is the source code for the framework but in most cases, you will not need to modify it.
The other folder called modules can be used to store your source code for the interface.

If you open the file "main.py" you will see this:
```python
import CLIF_Framework.framework as framework
 
console = framework.console()
 
framework.module("modules.main", console)
 
console.run()
```

The line  `import CLIF_Framework.framework as framework` imports the framework itself.
After that, the line `console = framework.console()` sets the variable `console` to the console class which means that the variable `console` defines a new interface.
The line `framework.module("modules.main", console)` loads your script located under modules/main as an interpreter for the variable `console`.
The last line `console.run()` tells the interface `console` to start.
The main file calls the first console/interface which loads your script as the logic of the interface.
It is a bit complicated at first but should be clear later on.

You can just keep the file as is and have a view at the file modules/main.py:
```python
from CLIF_Framework.framework import event
event = event()

class Temp:
   def __init__(selfie, console):
      global self
      global var
      self = selfie
      var = console
      
      self.main()
   
   def main(self):
      # Put your event help, etc. in here.
      pass

def setup(console):
   console.add(Temp(console), event)
```

Here you can see the basic structure of a "module".

First, you will always need to import an event object:

``from CLIF_Framework.framework import event``

Then you will need to set the variable `event` to an instance of this class:

``event = event()``

The event object saves help messages, events, and commands you define.

It will then be passed to the console instance which will collect that information and call the specific definitions of the event object.

Now we create a class which you can call whatever you want:

```python
class Temp:
   def __init__(selfie, console):
      global self
      global var
      self = selfie
      var = console
```

The class in this case is called Temp.

To be able to globally use the important variables we will need a small workaround, though it is just a temporary solution.

```python
def __init__(selfie, console):
      global self
      global var
      self = selfie
      var = console
```

As you can see instead of calling the self argument `self` we call it `selfie` to prevent variable conflicts.

We rename the console object to var because it is shorter and we can use it to define variables globally but mostly you should be able to just use `self` instead.

Now you could create a function for all the stuff you would like to define:

```python
class Temp:
	def __init__(selfie, console):
		global self
		global var
		self = selfie
		var = console

		self.main() # To call the function

	def main(self):
		# Put your event help, etc. in here.
		pass
```

In this main function we will define our menu context using the inbuilt help functions:

```python
	def main(self):
		event.help("(1)", "Option number 1.")
		event.help("(1)", "Option number 1.")
		event.help_comment("Select an option.")
```

You will be able to understand them when we run the script for the first time.

Now we will need to show our help message and therefore we will need to import a tool kit for advanced inbuilt functions:

```Python
from CLIF_Framework.framework import event
from CLIF-Framework.framework import tools
event = event()
tools = tools()
```

Now lets display our help message:

```python
def main(self):
	event.help("(1)", "Option number 1.")
	event.help("(1)", "Option number 1.")
	event.help_comment("Select an option.")
	
    event.help_title("Menu")
    tools.help("", " :: ", event)
    # tools.help((STR-TO-PUT-IN-FRONT-OF-FIRST-LINE), (STR-TO-SPLIT-VALUES-WITH), (EVENT-OBJECT))
    # All of it is saved into event.help_list
```
It should be farily self explaining.

`tools.help` displays a help message.

Now that we have our menu we will need to grab the user input:

```python
class Temp:
	def __init__(selfie, console):
		...

	def main(self):
		...

	@event.command # event.command(function) would do the same
	def one():
		print("You selected one.")

	@event.command
	def two(command): # You can get the exact input by adding a first argument
		print("You selected two.")
```

The problem with this is that those functions will just run when you enter `one`  or `two`  and now `1` or `2`.

Because we want it to be called through a number input we will need a workaround:

```python
class Temp:
	def __init__(selfie, console):
		...

	def main(self):
		...
		event.commands(self.one, "1") # will only accept 1
		event.commands(self.two, ["2", "two"]) # Will accept both

	def one(self):
		print("You selected one.")

	def two(self):
		print("You selected two.")
```

Note that `event.command` and `event.commands` are different:

- `event.command` sets the command name based on the function name.
- `event.commands` sets the command name based on a second argument.

Lets continue with a basic event.

```python
class Temp:
	def __init__(selfie, console):
		...

	def main(self):
		...
		event.commands(self.one, "1") # will only accept 1
		event.commands(self.two, ["2", "two"]) # Will accept both

	def one(self):
		print("You selected one.")

	def two(self):
		print("You selected two.")
	
    event.event
    def on_command_not_found(command):
        print("Selection does not exist.")
```

There are inbuilt events but you can also create your own events and call them but that is a topic for later.

Now we just need to add the setup function.

It is always the same but necesairy:

```python
def console(console):
	console.ps1 = "Number: " # Change as you want
	console.add(Main(console), event)
```

Now you got everything you need for a simple menu:

```python
from CLIF_Framework.framework import event
from CLIF_Framework.framework import tools
event = event()
tools = tools()

class Menu:
	def __init__(selfie, console):
		global self
		global var
		self = selfie
		var = console
		
		self.main() # To call the function

	def main(self):
		event.help("(1)", "Option number 1.")
		event.help("(2)", "Option number 2.")
		event.help_comment("Select an option.")
	
    	event.help_title("Menu")
    	tools.help("", " :: ", event)
    	
    	event.commands(self.one, "1") # will only accept 1
		event.commands(self.two, ["2", "two"]) # Will accept both

	@event.event
	def on_command_not_found(command):
		print("This is not a valid selection, choose something from the list.")

	@event.event
	def on_command_found():
		var.stop() # Will stop asking for input

	def one(self):
		print("You selected one.")

	def two(self):
		print("You selected two.")

def setup(console):
	console.add(Menu(console), event)
```

Just run main.py and your done.

Output:

```
Menu
(1) :: Option number 1.
(2) :: Option number 2.
Select an option.
:: d
This is not a valid selection, choose something from the list.
:: 1
You selected one.
```

[Click here to view an example -->](https://github.com/Taguar258/CLIF/blob/master/docs/advanced.md)
