#To remove the key from a given DIctionary
d={'a':'Apple','B':'banana','c':'cat'}
print(d)
key=str(input('Enter the key'))
'''d.pop(key)
print(d)'''
if key in d:
        del d[key]
else:
    exit(0)
    d[key]=[]
print(d)
