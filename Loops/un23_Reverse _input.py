#write program to print a new a number with digits  reversed  as of original one
n=int(input('Ener the number'))
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
print(r)
