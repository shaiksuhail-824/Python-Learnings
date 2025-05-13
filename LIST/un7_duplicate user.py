n=int(input('Enter the lenght'))
l=[]
for i in range(0,n):
    element=int(input('enter the element'))
    l.append(element)
    dup=[]
    for i in l:
        if(i not in dup):
            dup.append(i)
print(dup)