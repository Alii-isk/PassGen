from generator import Generator, NumbersPlugin, SymbolesPlugin

num_REGEX = r"(\[(\d+)-(\d+)\])"  #[1-9]
symboles_range = r"(\[(\W+)+\])"  #[@,#,.]

def Ignore(line):
	return line.startswith("#") or  line.strip() == ""



res = []
config = open("extend.conf", 'r')
namesFile = open("names.txt","r")
passFile = open("passwords.txt","w")


g = Generator([
	NumbersPlugin(),
	SymbolesPlugin()
	])

for line in config:
	if Ignore(line.strip('\n')): continue
	for name in namesFile:
		line = line.strip('\n').replace("{name}",name.lower())
		# g.run(line)
		[ res.append(x) for x in g.run(line,None,0,0) ]


for r in res:
	passFile.write(r + "\n")
	passFile.write(r.upper() + "\n")







