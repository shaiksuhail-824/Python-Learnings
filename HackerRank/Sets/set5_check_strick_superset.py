'''set_A=set(map(int,input().split()))
Number_of_sets=int(input())
for i in range(Number_of_sets):
    set_B= set(map(int,input().split()))
    if set_A > set_B:
           if set_A.issuperset(set_B):
                   print("True")
                   
    else:
        print("False")'''
s={1,2,3,4,5}
for i in s:
    print(s[i])