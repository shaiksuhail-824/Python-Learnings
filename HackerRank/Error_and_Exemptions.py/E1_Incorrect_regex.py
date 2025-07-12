import re

N = int(input())
for i in range(N):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)