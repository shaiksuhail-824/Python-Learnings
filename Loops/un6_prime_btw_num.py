#Write a program to print all Prime numbers between 1 to n
n=int(input('enter a number'))
for i in range(1,n+1):
    s=0
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(i==s):
        print(i)

