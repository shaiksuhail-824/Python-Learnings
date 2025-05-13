#Write a program to find all duplicates in the list
l=[5,10,1,2,22,3,1,2,3,7]
dups=[]
count=0
for i in l:
    for j in l:
        if(i==j):
            count=count+1
        if(count>1):
            if  i not in dups:
              dups.append(i)
    count=0
print(dups)
'''
for i in l:
    if(l.count(i)>1):
        if(i not in dups):
            dups.append(i)
print(dups)
'''