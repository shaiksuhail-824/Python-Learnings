#Write a program to print sum of all odd numbers between two intravel given.
a=int(input('Enter a number'))
b=int(input('Enter a number'))
s=0
for i in range(a,b+1):
    if(i%2!=0):
        s=s+i
print(s)