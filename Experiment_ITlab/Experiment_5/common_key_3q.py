d1={'a':100,'b':200,'c':300,'e':700}
d2={'a':300,'b':200,'d':400}
print(d1)
print(d2)
d3={}
for i,j in d1.items():
    d3[i]=j
for i,j in d2.items():
    if(i in d3):
        d3[i]=d3[i]+j
    else:
        d3[i]=j
print(d3)