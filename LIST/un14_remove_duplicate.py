#A program to remove duplicate element  from a given list
l=input('enter the Element')
k=len(l)
l1=[]
for i in l:
    if i not in l1:
      l1.append(i)
print(l1)