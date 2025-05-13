'''
Write a program that takes a list of numbers and returns the cumulative sum;
that is, a new list where the ith element is the sum of the first i+1 elements from the original list.
For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
'''
l=[5,8,10,15,20,25]
l1=[]
sum=0
print(l)
for i in l:
    sum=sum+i
    l1.append(sum)
print(l1)