import importlib

class console_read_only(type):
	def __setattr__(self, name, value):
		if attr == "objects":
			raise Exception("Variable cannot be called objects.")

class console:
	__metaclass__ = console_read_only
	def __init__(self):
		self.objects = []
		self.ps1 = ":: "
	def add(self, object, event):
		self.objects.append([object, event])
	def run(self):
		for object in self.objects:
			event_object = object[1]
			for event in event_object.events:
				if event.__name__ == "on_start":
					event()
			for event in event_object.events:
				if event.__name__ == "on_ready":
					event()


		while True:
			console_command = input(self.ps1)
			for object in self.objects:
				event_object = object[1]
				for command in event_object.commands:
					if command.__name__ == console_command.split(" ")[0]:
						parser_exists = False
						for parser in event_object.parsers:
							if type(parser[0]) == type([]):
								for parser_command in parsers[0]:
									if parser_command[0] == command.__name__:
										command(parser_command[1](console_command))
										parser_exists = True
										break
								if parser_exists:
									break
							elif type(parser[0]) == type(""):
								if parser[0] == command.__name__:
									command(parser[1](console_command))
									parser_exists = True
									break
						try:
							if not parser_exists: command(console_command=str(console_command))
						except:
							command()

def module(module, console):
	new = importlib.import_module(module)
	new.setup(console)
	del(new)

def arg(label, comname, com):
	if len(com.split("%s " % comname)) == 2:
		if com.split("%s " % comname)[1] == "":
			zw = input("%s" % label)
		else:
			zw = com.split("%s " % comname)[1]
			print("%s%s" % (label, zw))
	else:
		zw = input("%s" % label)
	return zw

class event:
	def __init__(self):
		self.events = []
		self.commands = []
		self.parsers = []

	def log(self):
		print("Events:", self.events)
		print("Commands:", self.commands)
		print("Parsers:", self.parsers)

	def event(self, function):
		self.events.append(function)
	def command(self, function):
		self.commands.append(function)
	def parser(self, command, function):
		self.parsers.append([command, function])