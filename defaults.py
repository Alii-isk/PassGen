import argparse


symbols = ['.','!','@','#','$','&','-','_','.',' ','+']
res = []
baseWord = "brahim"
append = ["abc","abcd","123","1234","0123","wifi","password","AA","Aa","AB"]


def passFromDates():
	_pass = []
	for date in range(1950,2050):
		_pass.append(str(date) * 2)	#20002000
		_pass.append(str(date) * 3)	#200020002000
  
		for ap in append:
			_pass.append(str(date) + ap)
			_pass.append(str(date) * 2 + ap)
			_pass.append(ap + str(date))
			_pass.append(ap + str(date) * 2 )

		for s in symbols:
			for n in range(0,4):
				_pass.append((s * n) + str(date) + (s * n) )	#@@@@2000@@@@
				_pass.append((s * n) + str(date) )	#a@@@@2000
				_pass.append(str(date)  +  (s * n) +  str(date)  )	#2000ali2000
	 
	 
				for ap in append:
					_pass.append((s * n) + str(date) + (s * n) + ap )
					_pass.append((s * n) + str(date) )
					_pass.append(str(date)  +  (s * n) +  str(date)  + ap )
	 
			#@@##2000####
			for s2 in symbols:
				for n in range(0,4):
					_pass.append(s + str(date) + ( s2 * n) )	#@2000#
					_pass.append( (s * 2) +  str(date) + ( s2 * n) )	#@@2000#
					_pass.append( (s * 3) +  str(date) + ( s2 * n) )	#@@@2000#
					_pass.append( (s * 4) +  str(date) + ( s2 * n) )	#@@@@2000#
					_pass.append(str(date) + ( s2 * 4))	#2000@@@@
					_pass.append(str(date) + ( s2 * 5))	#
					_pass.append(str(date) + ( s2 * 6))	#
					_pass.append(str(date) + ( s2 * 7))	#
					_pass.append(str(date) + ( s2 * 8))	#
	  
					_pass.append( ( s2 * 4) + str(date))	#@@@@2000
					_pass.append( ( s2 * 5) + str(date))	
					_pass.append( ( s2 * 6) + str(date))	
					_pass.append( ( s2 * 7) + str(date))	
					_pass.append( ( s2 * 8) + str(date))
	  
	  
	  
				for ap in append:
					_pass.append(s + str(date) + ( s2 * n)  + ap)
					_pass.append( (s * 2) +  str(date) + ( s2 * n) + ap )
					_pass.append( (s * 3) +  str(date) + ( s2 * n) + ap )
					_pass.append( (s * 4) +  str(date) + ( s2 * n) + ap )
					_pass.append(str(date) + ( s2 * 4) + ap)	
					_pass.append(str(date) + ( s2 * 5) + ap)
					_pass.append(str(date) + ( s2 * 6) + ap)
					_pass.append(str(date) + ( s2 * 7) + ap)
					_pass.append(str(date) + ( s2 * 8) + ap)
	  
					_pass.append( ( s2 * 4) + str(date) + ap)
					_pass.append( ( s2 * 5) + str(date) + ap)
					_pass.append( ( s2 * 6) + str(date) + ap)
					_pass.append( ( s2 * 7) + str(date) + ap)
					_pass.append( ( s2 * 8) + str(date) + ap)
	 
	


	for j in range(1950,2050):
		_pass.append(str(date) + str(j))
		for s in symbols:
			for n in range(0,4):
				_pass.append(str(date) +(s * n) + str(j))
				_pass.append((s * n) + str(j) + str(j))
				_pass.append(str(j) + str(j) +(s * n))
			for ap in append:
				_pass.append(str(date) +(s * n) + str(j) + ap)
				_pass.append((s * n) + str(j) + str(j) + ap)
				_pass.append(str(j) + str(j) +(s * n) + ap)
	 
				_pass.append(ap + str(date) +(s * n) + str(j) )
				_pass.append(ap + (s * n) + str(j) + str(j) )
				_pass.append(ap + str(j) + str(j) +(s * n) )
	
	passwords = [x for x in sorted(set(_pass)) if len(x)>=8]
	for p in passwords:
		res.append(p)

def pass2():
	_pass = []
	for s in symbols:
		for ap in append:
			_pass.append(s + ap )
			_pass.append(s + ap )

	passwords = [x for x in sorted(set(_pass)) if len(x)>=8]
	for p in passwords:
		res.append(p)


def guessSpecialsOnly():
	_pass = []
	for i in symbols:
		for a in range(8,12):
			_pass.append(str(i) * a)
	
	passwords = [x for x in sorted(set(_pass)) if len(x)>=8]
	for p in passwords:
		res.append(p)


def caseToggle():
	print("case toggle")
	with open("defaults.txt","a") as f:
		for p in  res:
			f.write(p.upper() + "\n")
			f.write(p.capitalize() + "\n")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-o')
	args = parser.parse_args()
	# print(args.o)
	# exit(0)
	passFromDates()
	pass2()
	guessSpecialsOnly()

	with open(f"{args.o}.txt","w") as f:
		for p in  sorted(set(res)):
			f.write(p + "\n")
	caseToggle()
	print("[+] Defaults Generated!")