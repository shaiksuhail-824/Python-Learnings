n=int(input('Enter no. of students'))
d={}
for i in range(n):
    a=input('Enter student name:')
    b=int(input('Enter student score'))
    d[a]=b
print(d)
def high():
    m=0
    for i in d:
        if(d[i]>m):
            m=d[i]
    for j,k in d.items():
        if(k==m):
            print('THe high score student is:',j,k)
high()