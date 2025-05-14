'''
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
'''
string=str(input('Enter the string'))
dict={}
for i in string:#easy
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
print(dict)
'''l=[]
l=string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))'''