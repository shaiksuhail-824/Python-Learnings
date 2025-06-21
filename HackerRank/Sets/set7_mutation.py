# Enter your code here. Read input from STDIN. Print output to STDOUT
'''number_of_element=int(input())
number_of_element_set=set(map(int,input().split()))
number_of_other_sets=int(input())
for i in range(number_of_other_sets):
    operation_name=map(str,input().split())
    operation_name=list(operation_name)
    if operation_name[0]=="intersection_upadate":
        number_of_element_set1=set(map(int,input().split()))
        number_of_element_set.intersection_upadate(number_of_element_set1)
    elif operation_name[0]=="update":
        number_of_element_set2=set(map(int,input().split()))
        number_of_element_set.update(number_of_element_set2)
    print(number_of_element_set)'''
'''elif operation_name[0]=="symmetric_difference_update":
        number_of_element_set3=set(map(int,input().split()))
        number_of_element_set.symmetric_difference_update(number_of_element_set3)
    elif operation_name[0]=="difference_udpdate":
        number_of_element_set4=set(map(int,input().split()))
        number_of_element_set.difference_update(number_of_element_set4)
print(sum(number_of_element_set))'''
set1={ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24,52,}
set2= {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}
set1.intersection_update(set2)
print(set1)
