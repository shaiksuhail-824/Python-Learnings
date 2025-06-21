number_of_sets=int(input())
for _ in range(number_of_sets):
    number_of_elements_in_set=int(input())
    set_A = set(map(int, input().split()))
    number_of_elements_in_set=int(input())
    set_B = set(map(int,input().split()))
    if set_A.issubset(set_B):
        print("True")
    else:
        print("False")
