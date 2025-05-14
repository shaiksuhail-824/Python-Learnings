#Write a program to swap two numbers without using a temporary variable.
a=(15,30)
b=(1,2)
b,a=a,b
print(a,b)
n=int(input('enter the lenght'))
t=()
for i in range(0,n):
    element=int(input('enter the element'))
    t=t+(element,)
print(t)