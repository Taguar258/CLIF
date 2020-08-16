### All functions:

-------------------

Here you will find all functions and classes listed below:

|       Function        |                         Description                          |                            Usage                             |        Type        |
| :-------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------: |
|       console()       |               Create a new interface instance.               |                     console = console()                      |       Class        |
|       module()        |                Add a module to an interface.                 |         module("module_path_split_by_dot", console) #Pass additional arguments.         |      Function      |
|     console.run()     |                Show  and start the interface.                |                        console.run()                         | Function of class  |
|    console.objects    |                   All modules and events.                    |                             List                             | Variable of class  |
|      console.ps1      |                         Input text.                          |                  Variable (default: ":: ")                   | Variable of class  |
| console.command_split |          Char that will be used to split commands.           |                   Variable (default: " ")                    | Variable of class  |
|    console.running    |           Set to false to interrupt the main loop.           |                   Boolean (default: True)                    | Variable of class  |
|   self.command_log    |                Logs all events and commands.                 |                             List                             | Variable of class  |
| console.debug_command | If set to True it will show more information about commands. |                   Boolean (default: False)                   | Variable of class  |
|  console.run_command  |      Is used as an cache for running commands manually.      |                             List                             | Variable of class  |
|     console.add()     |            Adds a module's class to an interface.            |           console.add(Class_Name(console), event)            | Function of class  |
|    console.stop()     | Sets console.running to False to nicely stop interface's execution. |          console.stop() or console.running = False           | Function of class  |
|    console.input()    |  Next command input will be set to the function's argument.  | console.input("command_name", True)  \|  (True to show input; False to hide input) | Function of class  |
|    console.event()    |             Run an event, may be defined by you.             |                 console.event("event_name")                  | Function of class  |
|        tools()        |            Class that contains helpful functions.            |                       tools = tools()                        |       Class        |
|      tools.arg()      |     Convert command input to input without command name.     | variable = arg("Title for variable input", "command name with space at the end", command) | Fucntion of class  |
|     tools.help()      |  Grabs the defined help messages of event and prints them.   | tools.help("first line", "chars to split command from value", event) | Function of class  |
|   tools.question()    |                   Simple Yes or No input.                    |  bool_variable = tools.question("Do you want to continue?")  | Fucntion of class  |
|        event()        |      Class that defines and passes events and commands.      |                       event = event()                        |       Class        |
|  event.event_events   |                     All defined events.                      |                             List                             | Variable of class  |
| event.event_commands  |                    All defined commands.                     |                             List                             | Variable of class  |
|  event.event_parsers  |                     All defined parsers.                     |                             List                             | Variable of class  |
|    event.help_list    |                   All defined help values.                   |                             List                             | Varibale of class  |
| event.help_text_title |                 Defined help message title.                  |                String (Empty string for none)                | Variable of class  |
|      event.log()      |        Prints some information about an event object.        |                         event.log()                          | Function of class  |
|     @event.event      | Designed to work with decorators to create custom and inbuild event functions. |                    event.event(function)                     | Function of class  |
|    @event.command     | Designed to work with decorators to create custom commands.  |                   event.command(function)                    | Function of class  |
|   event.commands()    | Asign mutliple commands to a function or use it to create command names that cannot match python's function naming rules. | event.commands(command_function, string_or_list_for_command_names) | Function of class  |
|    event.parser()     | Add a parser which passes commands to those functions as argument and returns as argument to command function. |            event.parser(function, "command_name")            | Function of class. |
