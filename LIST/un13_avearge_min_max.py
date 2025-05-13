n=int(input('enter the lenght'))
l=[]
for i in range(0,n):
    element=int(input('Enter the element'))
    l.append(element)
print(l)
print(min(l))
print(max(l))
print(sum(l)/len(l))
