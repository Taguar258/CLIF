import framework.framework as framework

console = framework.console()

import modules.ping as new
new.setup(console)
del(new)

print(console.objects)

console.run()