''''''
Write a Python program to get all unique combinations of two Lists.
Example:
list1 = [22, 23, 24, 25, 26]  
list2 = [23, 25, 27, 29]  
Output = [23, 25]
'''
l1=[22,23,24,25,26]
l2=[5,8,10,15,20,25]
l3=[]
for i in l1:
    for j in l2:
        if(i==j):
            l3.append(i)
print(l3)
'''for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
         l3.append(l1[i])
print(l3)'''

