
size_of_each_room = int(input())
unordered_rooms = list(map(int,input().split()))
from collections import Counter
count=Counter(unordered_rooms)
for num,freq in count.items():
    if freq==1:
        print(num)