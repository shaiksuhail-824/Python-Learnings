#Write a program that accepts a string from user 
#and redisplays the same string after removing vowels from it?
s='hihellohowareyou'
v='aeiouAEIOU'
s1=''
for i in s:
    if(i not in v):
        s1=s1+i
print(s1)
v='a'
for i in s:
    if(i==v):
        s.remove(i)
print(s)