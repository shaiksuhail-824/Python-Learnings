
l=[45,6,32,90,56,25,12,78]
s=l[0]
s2nd=l[0]
for i in l:
    if(i<s):
         s=i
for k in l:
    if(k!=s2nd):
         s2nd=k
for j in l:
       if(j<s and j<s2nd):
            s2nd=j
print('second smallest value',s,)
