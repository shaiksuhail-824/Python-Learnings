#Create a list of tuples from given list having number and its cube in each tuple.
n1=int(input('Enter the number'))
n2=int(input('Enter the number'))
a=[(i,i**3) for i in range(n1,n2+1)]
print(a)