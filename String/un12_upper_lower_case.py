#Python Program to Read a List of Words and Return the Length of the Longest One?
s='RGUKtongRKV'
a=0
b=0
for i in s:
    if(i.isupper()):
        a=a+1
    elif(i.islower()):
        b=b+1
print('upper:',a,'lower',b)