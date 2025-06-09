n = int(input())
s = set(map(int, input().split()))
n1=int(input())
for i in range(n1):
    command=map(str,input().split())
    command=list(command)
    if command[0]=='pop':
        s.pop()
    elif command[0]=='remove':
        s.remove(int(command[1]))
    elif command[0]=='discard':
        s.discard(int(command[1]))

print(s)