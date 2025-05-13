#Print perfect cube
n=int(input('Enter the number'))
for i in range(1,n):
    if(i*i*i==n):
        print('it is perfect square number')
        break
else:
        print('it is not perfect square number')