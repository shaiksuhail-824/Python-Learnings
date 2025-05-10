a=int(input("Enter a number"))
b=int(input('Enter a number'))
c=int(input('Enter a number'))
d=[13,14,16,17,18,19]
if(a in d and b in d and c in d):
   print("0")
elif(a in d and b in d):
   print(int(c))
elif(b in d and c in d):
   print(a)
elif(c in d and a in d):
    print(b) 
elif(a in d):
   print('the value is' ,(b+c))
elif(b in d):
   print('the value is' ,(a+c))
elif(c in d):
   print(a+b)
elif(a not in d and b not in d and c not in d):
   print(a+b+c)



