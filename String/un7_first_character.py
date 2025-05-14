#To find the first character from given string, count the number of times repeated and replaced with * except
#first character then print final string?
s='hihellohowareyou'
f=s[0]
m=s[1:].replace(f,'*')
print(f+m)
