from generator import Generator, NumbersPlugin, SymbolesPlugin

num_REGEX = r"(\[(\d+)-(\d+)\])"  #[1-9]
symboles_range = r"(\[(\W+)+\])"  #[@,#,.]

def Ignore(line):
	return line.startswith("#") or  line.strip() == ""



res = []
config = open("extend.conf", 'r')

g = Generator([
	NumbersPlugin(),
	SymbolesPlugin()
	])

for line in config:
	if Ignore(line.strip('\n')): continue
	line = line.strip('\n').replace("{name}","ahmed")
	# g.run(line)
	[ res.append(x) for x in g.run(line,None,0,0) ]

print(res)
print("done")



