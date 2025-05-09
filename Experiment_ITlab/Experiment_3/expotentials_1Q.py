base=int(input('Enter the base'))
exp=int(input('Enter the expo'))
a=1
for i in range(1,exp+1):
    a=base*a
    
print(a)