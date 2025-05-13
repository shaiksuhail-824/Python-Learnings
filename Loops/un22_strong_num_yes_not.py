# write a program to find given  numbers is strong number or not
i=int(input('Ener the number'))
n=i
sum=0
while(n<0):
    a=n%10
    b=1
    for j in range(1,a+1):
        b=b*j
    sum=sum+b
    n=n//10
if(i==sum):
    print(i,'it is strong number')
else:
    print(i,'it is not strong number')