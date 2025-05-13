# write a program to find the LCM of two numbers
n1=int(input('Ener the number'))
n2=int(input('Ener the number'))
for i in range(1,n1*n2+1):
    if(i%n1==0 and i%n2==0):
        print(i)
        break