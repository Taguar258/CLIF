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
		self.command_split = " "
		self.running = True
		self.command_log = []
		self.debug_command = False
	def add(self, object, event):
		self.objects.append([object, event])
	def stop(self):
		self.running = False
	def _run_event(self, name):
		self.command_log.append(str(name))
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
		self.running = True
		self._run_event(["on_start", "on_ready"])


		while self.running:
			try:
				console_command = input(self.ps1)
			except:
				self._run_event("on_interrupt")
				break
			if console_command == "" or console_command == " ":
				continue

			self._run_event("on_command")

			self.command_log.append(str(console_command))

			for object in self.objects:
				event_object = object[1]
				for command in event_object.event_commands:
					if self.debug_command:
						print(command[0].replace("_", self.command_split), console_command.split(self.command_split)[0])
					if command[0].replace("_", self.command_split) == console_command.split(self.command_split)[0]:
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
							if not parser_exists: command[1](console_command)
						except:
							command[1]()


def module(module, console, *args):
	new = importlib.import_module(module)
	if len(args) == 0:
		new.setup(console)
	else:
		new.setup(console, args)
	del(new)

class tools:
	def __init__(self):
		pass

	def arg(self, label, comname, com):
		if len(com.split(comname)) == 2:
			if com.split(comname)[1] == "":
				zw = input("%s" % label)
			else:
				zw = com.split(comname)[1]
				print("%s%s" % (label, zw))
		else:
			zw = input("%s" % label)
		return zw

	def help(self, startline, splitter, event):
			max_len = 0
			for help in event.help_list:
				if type(help[0]) == type([]):
					if len(", ".join(help[0])) > max_len:
						max_len = len(", ".join(help[0]))
				elif type(help[0]) == type(""):
					if len(help[0]) > max_len:
						max_len  = len(help[0])
			for help in event.help_list:
				if "[" in help[0]:
					split_help = help[0].strip('][').split(', ')
					help[0] = (", ".join(split_help[:-1]) + " or " + split_help[-1]).replace("'", "")
				length = (" " * (max_len - len(help[0])))
				print(startline + ("%s%s" % (length, splitter)).join(help))

class event:
	def __init__(self):
		self.event_events = []
		self.event_commands = []
		self.event_parsers = []
		self.help_list = []

	def log(self):
		print("Events:", self.event_events)
		print("Commands:", self.event_commands)
		print("Parsers:", self.event_parsers)
		print("Help:", self.help_list)
		
	def event(self, function):
		self.event_events.append(function)
	def command(self, function):
		self.event_commands.append([function.__name__, function])
	def help(self, function_name, message):
		if type(function_name) == type([]):
			self.help_list.append([str(function_name), message])
		elif type(function_name) == type(""):
			self.help_list.append([function_name, message])
	def commands(self, function, lt):
		if type(lt) == type([]):
			for name in lt:
				self.event_commands.append([name, function])
		elif type(lt) == type(""):
			self.event_commands.append([lt, function])
	def parser(self, function, command):
		self.event_parsers.append([command, function])

get_tools = tools()
get_event = event()