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