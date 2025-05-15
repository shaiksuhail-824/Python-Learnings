print('Python Calculator')
num1=int(input('Enter the First  number:-'))
print(' Press 1 for Addition  \n press 2 for Subraction  \n press 3 for Multplication \n Press 4 for  Division \n press 5 for Modulus \n press 6 for floor division' )
operation=str(input())
num2=int(input('Enter the Second number:-'))
if(operation=='1'):
    print(f'{num1}+{num2} =',num1+num2)
elif(operation=='2'):
    print(f'{num1}-{num2} =',num1-num2)
elif(operation=='3'):
    print(f'{num1}*{num2} =',num1*num2)
elif(operation=='4'):
    print(f'{num1}/{num2} =',num1/num2)
elif(operation=='5'):
    print(f'{num1}%{num2} =',num1%num2)
elif(operation=='6'):
    print(f'{num1}//{num2} =',num1//num2)
else:
    print('Invalid input')

