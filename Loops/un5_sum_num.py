#Write a program to enter any number and calculate sum of its digits
n=int(input('enter the number'))
s=0
while(n>0):
    i=n%10
    s=s+i
    n=n//10
print(s)