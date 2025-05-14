#Python program to create List of tuples with the
#First Element as the number and second Element as the square of number
num=int(input('enter the number'))
num2=int(input('enter the number'))
a=[(i,i**2) for i in range(num,num2+1)]
print(a)