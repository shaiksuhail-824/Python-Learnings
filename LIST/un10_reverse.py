#Read a list of n elements. Pass this list to a function which 
# reverses this list in-place without creating a new list.
l=[10,50,70,55,'ong']
#l.reverse()
#print(l)
print(l[::-1])
r=[]
for i in l:
    r=[i]+r
print(r)
