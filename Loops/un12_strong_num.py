#Write a program to print all Strong numbers between 1 to n.
p=int(input('enter the number'))
for i in range(1,p+1):
    n=i
    sum=0
    while(n>0):
        a=n%10
        b=1
        for j in range(1,a+1):
            b=b*j
        sum=sum+b
        n=n//10
    if(i==sum):
        print(sum)
"""
srong numbers-1,2,145,40585
145
1!=1
4!=24
5!=120
145
"""