#Write a program to enter any number and find its first and last digit.
n=int(input('enter the number'))
j=n%10
i=n
while(i>=10):
    i=i//10
print('last number',j)
print('first number',i)