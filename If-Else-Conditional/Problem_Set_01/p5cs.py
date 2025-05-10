a=int(input('Enter a number'))
b=int(input('Enter a number'))
c=int(input('Enter a number'))
if(a==b and b==c and c==a):
    print(0)
elif(a==b):
  print(c)
elif(a==c):
   print(b)
elif(b==c):
 print(a)
else:
   print(a+b+c)



