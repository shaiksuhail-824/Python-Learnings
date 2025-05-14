'''
pyton program to check if a given key Exits in aDictionary or not
'''
d={1:'A',2:'B',3:'C'}
key=input('ENter the key to check')


if key in d.keys():
    print('key is presnt in d')
    print(d[key])
else:
    print('key is not present')