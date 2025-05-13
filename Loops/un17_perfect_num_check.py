# Write a program to print the perfect number or not  
n=int(input('Enter the number'))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(n==sum):
    print('it is perfect')
else:
    print('it is not perfect')