#Write a program to read a list of elements. Modify this list so that it does not contain any duplicate elements,
#  i.e., all elements occurring multiple times in the list should appear only once.
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