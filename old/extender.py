import argparse
import time
import os
import re


parser = argparse.ArgumentParser()
parser.add_argument('-o')
parser.add_argument('--extend')
num_range = r"(\[(\d+)-(\d+)\])"  #[1-9]
symboles_range = r"(\[(\W+)+\])"  #[@,#,.]
res = []
config = open("extend-defaults.conf", 'r')


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
	foundsNum = re.findall(num_range, line)
	print(foundsNum)
	_res = []
	if len(foundsNum) > idx:
		for s1 in range(int(foundsNum[idx][1]),int(foundsNum[idx][2]) + 1):
			d1 =line.replace(foundsNum[idx][0],str(s1))
			#can we go deeper
			if len(foundsNum) > idx + 1:
				[ _res.append(x) for x in fillNumbers(d1,idx + 1) ]
			else:
				print("no more numbers ")
				if callbacks[idx]['check'](d1):
					[ _res.append(x) for x in callbacks[idx]['func'](d1,idx+1) ]
				else:
					_res.append(d1)
			# else :
				#foundsSym = re.findall(symboles_range, line)
				# if len(foundsSym) > 0:
				# 	[ _res.append(x) for x in fillSymbols(foundsSym,line,d1,0) ]
	return _res


def SymbolsCheck(line):
	foundsSym = re.findall(symboles_range, line)
	print("chekning symboles : ",len(foundsSym) > 0)
	return len(foundsSym) > 0

def fillSymboles(line,idx):
	foundsSym = re.findall(symboles_range, line)
	print("symbols")
	pass
	# _res = []
	# if len(foundsSym) > idx:
	# 	for s1 in foundsSym[idx][1].split(","):
	# 		d1 = ""
	# 		if c == None: d1 = line.replace(foundsSym[idx][0],str(s1))
	# 		else: d1 = c.replace(foundsSym[idx][0],str(s1))
  	# 		#can we go deeper
	# 		if len(foundsSym) > idx + 1:
	# 			[ _res.append(x) for x in fillSymbols(foundsSym,line,d1,idx + 1) ]
	# 		else : _res.append(d1)
	# return _res




callbacks = [
	{
		"func":fillSymboles,
		"check":SymbolsCheck
	}
]
def fillOut(line):
	# fillNumbers(line,0)
	[ res.append(x) for x in fillNumbers(line,0) ]



#from date
def Generate(n):
	res = []
	for line in config:
		if Ignore(line.strip('\n')): continue
		line = line.strip('\n').replace("{name}",n)
		fillOut(line)
  

	

#numbers : go through list and 
#
#
#
















if __name__ == '__main__':
	t0 = time.time()
	# names_file = open(f"{args.extend}","r")
	# for name in names_file:
	Generate("ahmed")
	print(res)
	# names_file.close()
	# passwords = [x for x in sorted(set(res)) if len(x)>=8] #remove duplicates & min-length is 8
	# print(res)
	# wordlist_file = open(f"{args.o}.txt",'w')
	# [wordlist_file.write(_pass + "\n") for _pass in res ]
	# wordlist_file.close()
	# config.close()
	print("[+] Done!")
	print("Time elapsed: ", time.time() - t0) # CPU seconds elapsed (floating point)
