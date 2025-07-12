import itertools
string_and_integer=list(map(str,input().split()))
string=string_and_integer[0]
integer=string_and_integer[1]
integer=int(integer)
s=[]
for i in string:
    s.append(i)
for i in range(1,integer+1):
        result=itertools.combinations(sorted(s),i)
        for i in list(result):
            print("".join(i))

