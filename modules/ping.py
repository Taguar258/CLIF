from framework.framework import event
from framework.framework import arg
event = event()

class Easy:
	def __init__(selfie, console):
		global var
		global self
		var = console
		self = selfie

		self.test = "test"

	@event.event
	def on_start():
		pass

	@event.command
	def ping(args):
		print(args)

	def ping_parse(command):
		return str(" ".join(command.split(" ")[1:]))
	event.parser("ping", ping_parse)

	@event.command
	def ping2(args):
		print(args)
		test = self.test

	def ping2_parse(command):
		return arg("Enter Text: ", "ping2", command)
	event.parser("ping2", ping2_parse)

def setup(console):
	console.add(Easy(console), event)