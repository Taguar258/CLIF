### Example:

-------------------------------------

This is basically a simplified module of the [Raven-Storm](https://github.com/Taguar258/Raven-Storm) toolkit wich was created by Taguar258 and created using the CLIF framework.

I will go through everything and explain each step using comments:

```python
from CLIF-Framework.framework import event # Import event
from CLIF-Framework.framework import tools # Import tools for importing prewritten stuff
from CLIF-Framework.framework import console # Used for starting new interface instances
from CLIF-Framework.framework import module # Used for starting new interface instances
from os import system # Library used for clearing the screen
event = event() # set event class to variable
tools = tools() # set tools class to variable

class Main:
	def __init__(selfie, console):
		global var    # Making global variable var
		global self   # Making global variable self
		self = selfie # Setting global variable self
		var = console # Setting global variable console

		var.modules = {} # Used for managing the interfaces
		self._add_commands() # Run functions to setup help etc.

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[34m"
		var.C_Dark_Blue = "\x1b[35m"
		var.C_Red = "\x1b[31m"
		var.C_Yellow = "\x1b[33m"
		var.C_Cyan = "\x1b[36m"

	def banner(self):
		print("Normally here would be the Raven-Storm Banner.")

	@event.event
	def on_ready(): # Inbuilt event run when on_start event done wich is run at start
		system("clear || cls") # clear screen
		self.banner() # Show banner
		self.help() # Showing the help message

	@event.event
	def on_command_not_found(command): # Inbuilt event run when command not existing
		print("")
		print("The command you entered does not exist.")
		print("")

	def exit_console(self): # Function to exit interface
		print("\033[1;32;0mHave a nice day.")
		quit()

	def _add_commands(self): # Setting up stuff
		event.commands(self.exit_console, ["exit", "quit", "e", "q"]) # Multiple commands exit the interface
		event.commands(self.run_shell, ".") # Function cannot be named .
		event.commands(self.debug, "$") # Function cannot be named $
		event.commands(self.help, "help") # Function will be called as command and by script
		event.parser(self.run_debug_arg, "$") # Add a parser function
		event.parser(self.run_shell_arg, ".") # Same here
		event.help(["exit", "quit", "e", "q"], "Exit Raven-Storm.")
		event.help("help", "View all commands.")
		event.help(".", "Run a shell command.")
		event.help("clear", "Clear the screen.")
		event.help("l4", "Load the layer4 module. (UDP/TCP)")
		event.help("l3", "Load the layer3 module. (ICMP)")
		event.help("scanner", "Load the scanner module.")
		event.help("flood", "Load a very simple but effective dos module.")

		var.modules["Layer4"] = console() # Create new interface instance
		var.modules["Layer3"] = console()
		var.modules["Scanner"] = console()
		var.modules["Flood"] = console()

	def run_shell(self, command):
		system(command)

	def run_shell_arg(self, command):
		return tools.arg("Enter shell command: \033[1;32;0m", ". ", command) # Inbuilt function to grab output.
		print("\033[1;32;0m", end="")

	def debug(self, command):
		eval(command)

	def run_debug_arg(self, command):
		return tools.arg("Enter debug command: \033[1;32;0m", "$ ", command)
		print("\033[1;32;0m", end="")

	@event.command # Simple command argument
	def l4():
		module("modules.l4.main", var.modules["Layer4"]) # Add module to new interface
		var.modules["Layer4"].run() # Start new interface / change screen.

	@event.command
	def l3():
		module("modules.l3.main", var.modules["Layer3"])
		var.modules["Layer3"].run()

	@event.command
	def scanner():
		module("modules.scanner.main", var.modules["Scanner"])
		var.modules["Scanner"].run()

	@event.command
	def flood():
		module("modules.downflood.main", var.modules["Flood"])
		var.modules["Flood"].run()

	def help(self):
		event.help_title("\x1b[1;39mHelp:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("\033[1;32;0m")

	@event.command
	def clear():
		system("clear || cls")

	@event.event # On command do:
	def on_command():
		print("\033[1;32;0m", end="")

	@event.event # On interrupt using for example CTRL + Z or CRTL + C
	def on_interrupt():
		self.exit_console()


def setup(console): # Setup function
	console.ps1 = "\033[1;32;0m>> " # Change text in front of command
	console.add(Main(console), event) # Add the class to the interface
```

[View all functions of CLIF -->](https://github.com/Taguar258/CLIF/blob/master/docs/everything.md)
