l=[67,23,6,51,90,45,8,3,83]
c=0
for i in l:
    c=c+1
l1=c
for i in range(1,l1+1):
    for j in range(l1-1):
        if(l[j+1]<l[j]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)