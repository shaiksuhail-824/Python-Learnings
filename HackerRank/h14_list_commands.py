n=int(input('ENter '))
l=[]
for i in range(1,n+1):
    l.append(i)
l.insert(1,0)
print(l)
l.append(8)
l.sort()
l.pop()
l.reverse()