import itertools
string_and_integer=list(map(str,input().split()))
string=string_and_integer[0]
integer=string_and_integer[1]
integer=int(integer)
s=[]
for i in string:
    s.append(i)
for i in range(integer+1):
        result=itertools.combinations(sorted(s),i)
        result=list(result)
        for i in result:
            print("".join(i))

