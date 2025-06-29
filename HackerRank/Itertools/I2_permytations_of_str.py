from itertools import permutations
string_and_integer=list(map(str,input().split()))
string=string_and_integer[0]
s=[]
for i in string:
    s.append(i)
integer=string_and_integer[1]
integer=int(integer)

result=list(permutations(s,integer))
result.sort()
for i in result :
    print("".join(i))