#Write a program to read a list of n integers and find their median.
#Note: The median value of a list of values is the middle value when the values are sorted.
l=[1,4,3,2,7,8,5,9,6]
l.sort()
l1=len(l)
print(l)
mid=(l1-1)//2
if(l1%2==0):
    print((l[mid]+l[mid+1])/2)
else:
    print(l[mid])