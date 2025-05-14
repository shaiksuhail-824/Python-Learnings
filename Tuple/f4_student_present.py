#Write a program to input names of n students and store them in a tuple.
# Also, input a name from the user and find if this student is present in the tuple or not.
#We can accomplish this by:
#(A) Using the built-in function
n=int(input('enter the lenght'))
t=()
for i in range(0,n):
    element=str(input('enter the element'))
    t=t+(element,)
print(t)
name=str(input('enter the name to find in tuple:'))
if(name in t):
    print('name is found')
else:
    print('name is  not found')


