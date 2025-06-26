import itertools
string=input().split()
print(string)
result=itertools.groupby(string,key = lambda x:x[0])
print(list(result))