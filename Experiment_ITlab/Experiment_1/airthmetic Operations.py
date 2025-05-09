x=int(input('Enter the number:' ))
y=int(input('ENter the number:'))
operands=str(input('ENter the operands: '))
if(operands=='+'):
    print('The result is :',x+y)
elif(operands=='-'):
    print('the result is :',x-y)
elif(operands=='*'):
    print('the result is :',x*y)
elif(operands=='/'):
    print('the result is :',x/y)
elif(operands=='%'):
    print('the result is :',x%y)
else:
    print('Invalid input')

