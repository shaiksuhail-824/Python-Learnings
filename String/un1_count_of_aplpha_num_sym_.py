#Write a program to find number of digits ,alphabets and symbols ?
s='rgukt123ong567rkv@#+*'
a=0
d=0
c=0
for i in s:
    if(i.isalpha()):
        a=a+1
    elif(i.isdigit()):
        d=d+1
    else:
        c=c+1
print('alphabet:',a,"Digits:",d,'symbol:',c)