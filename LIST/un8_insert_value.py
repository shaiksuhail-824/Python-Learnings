n=int(input('Enter the lenght'))
l=[]
for i in range(0,n):
    element=int(input('enter the element'))
    l.append(element)
print(l)
pos=int(input('enter the position'))
ele=int(input('enter the element to insert'))
l.insert(pos,ele)
print('new list:',l)