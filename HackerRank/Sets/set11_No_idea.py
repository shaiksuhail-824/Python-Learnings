array_of_n_and_m_integers = list(map(int,input().split()))
array=list(map(int,input().split()))
set_A=set(map(int,input().split()))
set_B=set(map(int,input().split()))
count=0
for i in array:
    if i in set_A :
        count=count+1
count_1=0

for i in array:
    if i in set_B:
        count_1=count_1+1
print(count-count_1)
