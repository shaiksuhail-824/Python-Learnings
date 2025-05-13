'''
Write a program to read elements of a list.

a) The program should ask for the position of the element to be deleted from the list.
 Write a function to delete the element at the desired position in the list.

b) The program should ask for the value of the element to be deleted from the list.
 Write a function to delete the element of this value from the list.
'''
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
