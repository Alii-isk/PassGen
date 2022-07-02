import argparse
import time
import re
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from functions.init import GetCallbacks

print(GetCallbacks())
parser = argparse.ArgumentParser()
parser.add_argument('-o')
parser.add_argument('--extend')
num_range = r"(\[(\d+)-(\d+)\])"  #[1-9]
symboles_range = r"(\[(\W+)+\])"  #[@,#,.]
res = []
config = open("extend-defaults.conf", 'r')
foundsNum = None


# args = parser.parse_args()
# if(args.o is None) or (args.extend is None):
# 	print("[-] args not found".title())
# 	exit(1)
# if not os.path.isfile(args.extend) and not args.extend.endswith('.txt'): # check if file exist
# 		print("[-] Extend option needs a txt file!".title())
# 		exit(1)
  
#replace a with @ and s with $
def Ignore(line):
	return line.startswith("#") or  line.strip() == ""

# def fillSymbols(foundsSym,line,c,idx):
# 	_res = []
# 	if len(foundsSym) > idx:
# 		for s1 in foundsSym[idx][1].split(","):
# 			d1 = ""
# 			if c == None: d1 = line.replace(foundsSym[idx][0],str(s1))
# 			else: d1 = c.replace(foundsSym[idx][0],str(s1))
#   			#can we go deeper
# 			if len(foundsSym) > idx + 1:
# 				[ _res.append(x) for x in fillSymbols(foundsSym,line,d1,idx + 1) ]
# 			else : _res.append(d1)
# 	return _res





def fillNumbers(line,idx):
	_res = []
	if len(foundsNum) > idx:
		for s1 in range(int(foundsNum[idx][1]),int(foundsNum[idx][2]) + 1):
			_line = line.replace(foundsNum[idx][0],str(s1))
			#can we go deeper
			if len(foundsNum) > idx + 1:
				[ _res.append(x) for x in fillNumbers(_line,idx + 1) ]
			else:
				print("no more numbers ")
				if len(callbacks) > idx and callbacks[idx]['check'](_line): #is there more modules
					[ _res.append(x) for x in callbacks[idx]['func'](_line,idx+1) ]
				else: _res.append(_line)
	return _res


def SymbolsCheck(line):
	foundsSym = re.findall(symboles_range, line)
	return len(foundsSym) > 0

def fillSymboles(line,idx):
	foundsSym = re.findall(symboles_range, line)
	print("symbols")
	pass



callbacks = [
	{
		"func":fillSymboles,
		"check":SymbolsCheck
	}
]
def fillOut(line):
	# fillNumbers(line,0)
	global foundsNum
	foundsNum = re.findall(num_range, line)
	[ res.append(x) for x in fillNumbers(line,0) ]
	print(res)
	foundsNum = None



#from date
def Generate(n):
	res = []
	for line in config:
		if Ignore(line.strip('\n')): continue
		line = line.strip('\n').replace("{name}",n)
		# fillOut(line)
  

















if __name__ == '__main__':
	t0 = time.time()
	Generate("ahmed")
	print(res)
	f = open("hello.txt","w")
	for i in res:
		f.write(i + "\n")
	f.close()
    
	print("[+] Done!")
	print("Time elapsed: ", time.time() - t0) # CPU seconds elapsed (floating point)
