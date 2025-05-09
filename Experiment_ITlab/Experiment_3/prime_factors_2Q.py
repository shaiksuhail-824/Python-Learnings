n=int(input('Enter the number'))
l=[]

for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
for x in l:
    c=0
    for y in range(1,1000):
        if(x%y==0):
            c=c+1
    if(c==2):
        print(x, end=" ")
       
