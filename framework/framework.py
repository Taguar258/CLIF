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

	def _run_event(self, name):
		if type(name) == type([]):
			for object in self.objects:
				event_object = object[1]
				for event in event_object.event_events:
					for n in name:
						if event.__name__ == n:
							event()
		elif type(name) == type(""):
			for object in self.objects:
				event_object = object[1]
				for event in event_object.event_events:
					if event.__name__ == name:
						event()

	def event(self, name):
		self._run_event(name)

	def run(self):
		self._run_event(["on_start", "on_ready"])


		while True:
			console_command = input(self.ps1)
			self._run_event("on_command")

			for object in self.objects:
				event_object = object[1]
				for command in event_object.event_commands:
					if command[0] == console_command.split(" ")[0]:
						parser_exists = False
						for parser in event_object.event_parsers:
							if type(parser[0]) == type([]):
								for parser_command in parsers[0]:
									if parser_command[0] == command[0]:
										command[1](parser_command[1](console_command))
										parser_exists = True
										break
								if parser_exists:
									break
							elif type(parser[0]) == type(""):
								if parser[0] == command[0]:
									command[1](parser[1](console_command))
									parser_exists = True
									break
						try:
							if not parser_exists: command[1](console_command=str(console_command))
						except:
							command[1]()

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
		self.event_events = []
		self.event_commands = []
		self.event_parsers = []
		self.event_help = []

	def log(self):
		print("Events:", self.event_events)
		print("Commands:", self.event_commands)
		print("Parsers:", self.event_parsers)
		print("Help:", self.event_help)
		
	def event(self, function):
		self.event_events.append(function)
	def command(self, function):
		self.event_commands.append([function.__name__, function])
	def help(self, function_name, message):
		if type(function_name) == type([]):
			self.event_help.append([", ".join(function_name), message])
		elif type(function_name) == type(""):
			self.event_help.append([function_name, message])
	def commands(self, function, lt):
		for name in lt:
			self.event_commands.append([name, function])
	def parser(self, command, function):
		self.event_parsers.append([command, function])