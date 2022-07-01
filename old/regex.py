import re

res = []














text = "[1-10]Ahmed[2010-2022]" 






















reg = r"(\[(\d+)-(\d+)\])" #the group of char a to c
founds = re.findall(reg, text)



def isRighLength(password):
   return len(password) >= 8


   
for n1 in range(int(founds[0][1]),int(founds[0][2]) + 1):
   c1 = text.replace(founds[0][0],str(n1))
   idx2 = 1
   for n2 in range(int(founds[idx2][1]),int(founds[idx2][2]) + 1):
      c2 = c1.replace(founds[idx2][0],str(n2))
      idx3 = idx2 + 1
      if(len(founds) > idx3):
         for n3 in range(int(founds[idx3][1]),int(founds[idx3][2]) + 1):
            c3 = c2.replace(founds[idx3][0],str(n3))
            if isRighLength : res.append(c3)
      else:
         if isRighLength : res.append(c2)
      


[ print(p) for p in res ]