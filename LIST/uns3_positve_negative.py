'''
Write a program to read a list of n integers (positive as well as negative).
Create two new lists:

one having all positive numbers

the other having all negative numbers
from the given list. Print both lists.


'''
l=[-1,5,-3,-7,8,11,25,-5]
p=[]
n=[]
print(l)
for i in range(1,len(l)):
    if(i>=0):
        p.append(i)
    else:
        n.append(i)
print('positve values:',p)
print('negative values:',n)