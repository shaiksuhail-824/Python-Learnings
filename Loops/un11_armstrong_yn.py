#Write a program to enter any number and check whether it is Armstrong number or not
n=int(input('Enter the number'))
temp=n
sum=0
while(n>0):
    i=n%10
    sum=sum+i**3 
    n=n//10
if(temp==sum):
    print('it is armstrong')
else:
    print('it is not armstrong')
"""" 
exam 3 digit likna
armstrong number:
153,371
1**3=3
5**3=125
3**3=27
153


"""