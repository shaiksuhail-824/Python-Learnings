M=int(input())
a=list(map(int,input().split()))
N=int(input())
b=list(map(int,input().split()))
a=set(a)
b=set(b)
x=a.difference(b)
y=b.difference(a)
for x in sorted(x):
    print(x)
for y in sorted(y):
    print(y)