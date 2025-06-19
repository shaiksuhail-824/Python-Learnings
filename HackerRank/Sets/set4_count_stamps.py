number_of_stamps =int(input())
stamps=set('')
for i in range(number_of_stamps):
    stamps_name=input()
    stamps.add(stamps_name)
#print(stamps)
l=list(stamps)
l1=[]
for i in l:
    if i not in l:
        l1.append(i)
count=0
for i in l:
    count=count+1
print(count)
