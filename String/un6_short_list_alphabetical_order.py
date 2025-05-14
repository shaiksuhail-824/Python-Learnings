#Write a program to sort list names in alphabetical order?
l=['bob','Charls','adams','jnon']
l1=len(l)
for i in range(1,l1+1):
    for j in range(l1-i):
        if(l[j+1]<l[j]):
         l[j],l[j+1]=l[j+1],l[j]
print(l)

