n=int(input('Enter the lenght'))
l=[]
for i in range(0,n):
    element=int(input('enter the element'))
    l.append(element)
print(l)
choise=int(input('enter the choise:'))
if(choise==1):
    pos=int(input('Enter the position no.'))
    l.pop(pos)
else:  
    ele=int(input('Enter the element to remove'))
    l.remove(ele)
print(l)
