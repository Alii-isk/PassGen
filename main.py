import argparse

symbols = ['.','!','@','#','$','&','-','_','.',' ','+']
res = []
append = ["abc","abcd","123","1234","0123","wifi","password",]


def passFromDates(base):
	_pass = []
	for date in range(1950,2050):
		_pass.append(base + str(date) + base )	#ali2000ali
		_pass.append(base + str(date))	#ali2000
		_pass.append(str(date) + base)	#2000ali
		_pass.append(str(date) + base + base)	#2000aliali
		_pass.append(base + base + str(date))	#aliali2000
		_pass.append(str(date) + base + base + base)	#2000alialiali
		_pass.append(base + base + base + str(date))	#alialiali2000
  
		for ap in append:
			_pass.append(str(date) + base + ap)
			_pass.append(ap + str(date) + base )

		for s in symbols:
			for n in range(0,4):
				_pass.append((s * n) + str(date) + base )	#@2000ali
				_pass.append(base + str(date) + (s * n) )	#ali2000@
				_pass.append(base + str(date) + (s * n) + base )	#ali2000@ali
				_pass.append(base + (s * n) + str(date) )	#ali@2000
				_pass.append(base + (s * n) + str(date) + (s * n) )	#ali@2000@
				_pass.append(base + base + str(date) + (s * n) )	#aliali2000
				_pass.append(base  +  (s * n) + base )	#aliali2000
				_pass.append(base  +  (s * n) + base + str(date)  )	#aliali2000
	 
	 
				for ap in append:
					_pass.append(base + str(date) + (s * n) + ap )
					_pass.append(base + str(date) + (s * n) + base + ap )
					_pass.append(base + (s * n) + str(date) + ap )
					_pass.append(base + (s * n) + str(date) + (s * n) + ap )
					_pass.append(base + base + str(date) + (s * n) + ap )
					_pass.append(base  +  (s * n) + base )
					_pass.append(base  +  (s * n) + base + str(date) + ap  )

	passwords = [x for x in sorted(set(_pass)) if len(x)>=8]
	for p in passwords:
		res.append(p)

def pass2(base):
	_pass = []
	for s in symbols:
		_pass.append(base + s + base )
		_pass.append(base + s )
		_pass.append(s + base )
		for ap in append:
			_pass.append(base + s + ap )
			_pass.append(base + ap )
			_pass.append(ap + s + base )
			_pass.append(ap + base + s )
			_pass.append(base + base + ap )
			_pass.append(base + ap + base )
			_pass.append(ap + base )
			_pass.append(base + ap )

	passwords = [x for x in sorted(set(_pass)) if len(x)>=8]
	for p in passwords:
		res.append(p)

def guess123(base):
	_pass = []
	_pass.append(base + '0000' )
	_pass.append(base + '00000')
	_pass.append(base + '000000')
	_pass.append(base + '00000000')
	for i in range(0,100000): #ali99999
		_pass.append(base + str(i) )
		_pass.append(str(i) + base )
	for k in symbols:
		for g in range(0,500):
			_pass.append(str(g) + str(k) + base )
			_pass.append(base + str(g) + str(k) )
			_pass.append(base + str(k) + str(g) )

			_pass.append(str(g) + str(k) + base + str(k) )
			_pass.append(base + str(g) + str(k) + str(k) )
			_pass.append(base + str(k) + str(g) + str(k) )
			_pass.append(str(k) + base + str(g) + str(k) )

	passwords = [x for x in sorted(set(_pass)) if len(x)>=8]
	for p in passwords:
		res.append(p)

def guessSpecialsOnly(base):
	_pass = []
	for i in symbols:
		for p in range(1,8):
			_pass.append(base + (str(i) * p))
	
	passwords = [x for x in sorted(set(_pass)) if len(x)>=8]
	for p in passwords:
		res.append(p)


def caseToggle():
	print("[*] Case Toggling ...")
	with open("pass.txt","a") as f:
		for p in  res:
			f.write(p.upper() + "\n")
			f.write(p.capitalize() + "\n")



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-o')
	parser.add_argument('--extend')
	args = parser.parse_args()
	print(args)
	if(args.o is None) or (args.extend is None):
		print('''
usage : script.py --extend name -o mypasswords 
--extend : name that you want to extend
-o : outputed wordlist name
        ''')
		args.o = "passwords"
		exit(1)
 
 
	print(f"[*] Generating Passwords for {args.extend}")
	passFromDates(args.extend)
	pass2(args.extend)
	guess123(args.extend)
	guessSpecialsOnly(args.extend)

	with open(f"{args.o}.txt","w") as f:
		for p in  sorted(set(res)):
			f.write(p + "\n")
	caseToggle()
 
print("[+] Done!")