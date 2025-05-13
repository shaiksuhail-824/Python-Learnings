a=int(input('enter the number: '))
b=int(input('enter the number: '))
c=int(input('enter the number: '))
if(a<b or c<b and a>c  ):
    print("the second smallest number is",a)
elif(b<c or a<c and b<a):
    print("the second smallest number is",b)
elif(c<a or b<a and c<b):
    print("the second smallest number is",c)
else:
    print('Enter 3 different no.')

