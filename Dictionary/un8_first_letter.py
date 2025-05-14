#Python Program to Create a Dictionary with Key as First Character
# and Value as Words Starting with that Character
d2=['Apple',"Ball","cat","Doll"]
dd={}
for i in d2:
    if(i[0] not in dd):
        dd[i[0]]=[]
        dd[i[0]].append(i)
print(dd)
    
