#Write a program to check whether given string is palindrome or not?
s=str(input('Enter the strings '))
s1=''
'''for i in s:
    s1=i+s1
print(s1)'''
'''s1=s[::-1]
'''
l=0
for i in s:
    l=l+1
print(l)
for i in range(1,l+1):
    s1=s1+s[l-i]
print(s1)
if(s==s1):
    print('it is palindrome ')
else:
    print('it is not palindrome')