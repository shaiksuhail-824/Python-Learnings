'''
Write a program to print the following output?
R
RG
RGU
RGUK
RGUKT
RGUK
RGU
RG
R
'''
s='RGUKT'
l=len(s)
for i in range(1,l+1):
    for j in range(i):
        print(s[j],end=" ")
    print()
for i in range(1,l+1):
    for j in range(l-i):
        print(s[j],end=" ")
    print()
            