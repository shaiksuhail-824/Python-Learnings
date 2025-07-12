import itertools
string_and_integer=list(map(str,input().split()))
string=string_and_integer[0]
integer=string_and_integer[1]
integer=int(integer)
s=[]
for i in string:
    s.append(i)
result=itertools.combinations_with_replacement(sorted(s),integer)
for i in list(result):
    print("".join(i))



