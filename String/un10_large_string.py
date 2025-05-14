#This is a Python Program to take in two strings and display the larger string
#  without using built-in functions.?
s1=str(input('enter the string1'))
s2=str(input('enter the string2'))
c1=0
c2=0
for i in s1:
    c1=c1+1
print(c1)
for i in s2:
    c2=c2+1
print(c2)
if(c1>c2):
    print(s1,'is larger')
elif(c1<c2):
    print(s2,' is larger')
elif(c1==c2):
    print('both are equal')
else:
    print('invalid input')

