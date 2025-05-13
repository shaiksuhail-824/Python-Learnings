# write a program to find the GCD of two numbers
n1=int(input('Ener the number'))
n2=int(input('Ener the number'))
if(n1>n2):
    min=n2
else:
    min=n1
for i in range(min,0,-1):
    if(n1%i==0 and n2%i==0):
     print(i)
     break