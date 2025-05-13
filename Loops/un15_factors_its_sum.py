#Print factors of given number and their sum
n=int(input('Enter the number'))
i=1
sum=0
while(i<=n):
    if(n%i==0):
        sum=sum+i
        print(i)
    i=i+1
print(sum)