#Write a program to input n numbers from the user. Store these numbers in a tuple. 
# Print the maximum and minimum number from this tuple.
n=int(input('enter the lenght'))
t=()
for i in range(0,n):
    element=int(input('enter the element'))
    t=t+(element,)
print(t)
print('Max:',max(t))
print('Min:',min(t))
