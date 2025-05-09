import random
l1=[3,91,6,89,16]
l2=[11,56,45,76,2,9,20]
l3=random.sample(l1,3)
l4=random.sample(l2,3)
l5=l3+l4
print('random list is :',l5)
primeno=[]
for i in l5:
    c=0
    for j in range(1,i):
        if(i%j==0):
           c=c+1
    if(c==1):
        print(i)
       # primeno.append(i)
#print(primeno)