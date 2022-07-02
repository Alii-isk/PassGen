import re
from generator import Generator,NumbersPlugin

num_REGEX = r"(\[(\d+)-(\d+)\])"  #[1-9]
symboles_range = r"(\[(\W+)+\])"  #[@,#,.]

def Ignore(line):
	return line.startswith("#") or  line.strip() == ""



def plugin1(*args):
	if len(args) == 1:
	 	#do your check here
		if args.regex: return "regex"
		return len( re.findall(num_range,  args[0])) > 0
	elif len(args) == 2:
		print("filling the plugins")
		return ["a","b","c"]
	else:
		print("[-] error args not correct".title())
		return []

def plugin2():
	print("plugin2")

def plugin3(*args):
	print("plugin3")



res = []
config = open("extend.conf", 'r')

g = Generator([
	NumbersPlugin(num_REGEX),
	])

for line in config:
	if Ignore(line.strip('\n')): continue
	line = line.strip('\n').replace("{name}","ahmed")
	# g.run(line)
	[ res.append(x) for x in g.run(line,None,0,0) ]

print(res)
print("done")



