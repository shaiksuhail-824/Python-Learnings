#Write a program to enter any number and display perfect numbers between 1 to n
n=int(input('enter the number'))
for i in range(1,n+1):
    s=0
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(s==i):
        print(i)

# n=int(input('enter the number: '))
# s=0
# for i in range(1,n+1):
#     if(n%i==0):
#         s+=i
# if(s==i):
#     print(n,'is a perfect number')
# else:
#     print(n,'not a perfect number')