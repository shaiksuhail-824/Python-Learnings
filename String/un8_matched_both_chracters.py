#To find the strings in a list which are matched with first character equals to last character in a string?
l=['bob','Charls','adams','jnon','mom']
print(l)
'''l1=[i for i in l if(i[0]==i[-1])]
print(l1)'''
l2=[]
for i in l:
 if(i[0]==i[-1]):
  l2.append(i)
print(l2)

