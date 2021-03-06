# CLIF Framework<br><img src="https://img.shields.io/badge/Language-Python3-blue"><img src="https://img.shields.io/badge/Status-Beta-orange"><img src="https://img.shields.io/badge/Version-1.1.5-red"><img src="https://img.shields.io/badge/Licence-MIT-yellowgreen">
**CLIF is a python framework for creating interactive command-line interfaces.**

CLIF aims to make code more human-readable.

CLIF can be optimized the way you want to make your ideas work.

<a href="https://github.com/Taguar258/CLIF#documentation">Download</a>

_I archived this repo because I am not happy with the implementation itself, I might be reworking this in feature but not for now._

## What has been created using CLIF?

<a style="color: grey" href="https://github.com/Taguar258/Raven-Storm/">Raven-Storm</a>

## What makes it different?
- [x] Inbuilt toolkit for common tasks.
- [x] Utilises python decorators.
- [x] Create events and call them later.
- [x] Quality over Quantity without thinking about it.
- [x] No installation is required.

## The difference
Normaly you would create if statements:
```python
command_input = input(">> ")

if command_input == "command1":
    pass
elif command_input == "command2":
    pass
else:
    print("Command does not exist.")
```

What it looks like using CLIF:
```python
@event.command
def command1(command):
    pass

@event.command
def command2(command):
    pass

@event.event
def on_command_not_found(command):
    print("Command does not exist.")
```

## Documentation

<a href="https://github.com/Taguar258/CLIF/blob/master/docs/">Click here for the Documentation.</a>

<a href="https://github.com/Taguar258/CLIF/releases/download/1.2/CLIF-Clean.zip">Download Template.</a>

<a href="https://github.com/Taguar258/CLIF/projects/1">Project status/ToDo</a>

<!--![Preview]()-->

**MIT Taguar258 2020**
