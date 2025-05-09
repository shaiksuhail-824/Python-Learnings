s=str(input('enter the string'))
w=s.split()
s1=' '
for i in w:
    if(i not in s1):
        s1=s1+i
        s1=s1+" "
print(s1)