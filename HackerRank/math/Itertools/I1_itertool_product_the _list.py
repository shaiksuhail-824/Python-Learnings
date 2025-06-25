import itertools
element_of_list_A=list(map(int,input().split()))
element_of_list_B=list(map(int,input().split()))
result=list(itertools.product(element_of_list_A,element_of_list_B))
for i in result :
    print(i,end=" ")