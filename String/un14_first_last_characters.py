#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a
#string. If the string length is less than 2, return instead of the empty string.
def mystring(s):
    if(len(s)<2):
     return ''
    return s[0:2]+s[-2:]
print(mystring('suhail'))
print(mystring('su'))
print(mystring('s'))
l='suhail'
s=''
if(len(l)<2):
      s=l[0:2]+l[-2:]
print(s)