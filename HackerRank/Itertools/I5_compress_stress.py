import itertools
string = list(map(str, input()))
for i in string :
    i = list(i)
    i.sort()
print(i)
result = itertools.groupby(i)
print(result)