#Write a program to read email IDs of n number of students and store them in a tuple.
#  Create two new tuples, one to store only the usernames from the email IDs and second to store domain names from the email IDs.
#  Print all three tuples at the end of the program.
#Hint: You may use the function split()


n=int(input('enter the lenght'))
t=()
for i in range(0,n):
    element=str(input('enter the element'))
    t=t+(element,)
print(t)
m=()
d=()
for i in t:
    t1=i.split('@')
    m=m+(t1[0],)
    d=d+(t1[1],)
print(m,end='')
print(d,end='')
