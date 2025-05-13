#Write a program to print Fibonacci series up to n terms.
n=int(input('enter the number'))
a=0
b=1
i=0
l=[]
while(i<=n):
    print(i,end=' ')
    l.append(i)
    a=b
    b=i
    i=a+b
print(l)
for i in l:
    if(reversed==True):
        print(i)

