import os
import importlib


print("init start >>>")
modules = []
#auto import all modules in current directory
for module in os.listdir(os.path.dirname(__file__)):
	if module == 'init.py' or module[-3:] != '.py':
		continue
	print(module)
	modules.append(importlib.import_module(module[:-3]))
del module



callbacks = []
for m in modules:
	if hasattr(m,'fill') and hasattr(m,'check'):
		callbacks.append({'func':m.fill,'check':m.check})
	else:
		print(f'''
        [-] Warning : module <{ m.__name__}> has no fill or check function
		  [-] the module will be ignored
        '''.title())
	
del modules




def GetCallbacks():
   print("init")
   return callbacks


print("init done")
