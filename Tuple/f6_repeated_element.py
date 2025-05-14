#TO find a repeated element in a tuple 
t=(1,3,5,2,1,6,5,4,8)
t1=()
t2=()
for i in t:
    if(i not in t1):
        t1=t1+(i,)
    else:
        t2=t2+(i,)
print("The repeated element",t2)