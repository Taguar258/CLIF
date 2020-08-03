import framework.framework as framework

console = framework.console()

framework.module("modules.ping", console)

print(console.objects)

console.run()