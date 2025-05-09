n= int(input('Enter the number'))
a=0
b=1
for  i in range(n-1):
    a,b=b,b+a
for i in range(n,0,-1):
    print(a,end=' ')
    a,b=b-a,a