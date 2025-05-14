#Write a Python program to find the highest 2 values in a dictionary.
d={'ong':550,'rkv':50,'nuz':750,'skl':800}
l=0
sl=0
for i in d:
    if(d[i]>l):
        sl=l
        l=d[i]
#for i in d:
    if(d[i]>sl and d[i]!=l):
        sl=d[i]
print('largest value',l,'second largest',sl)
