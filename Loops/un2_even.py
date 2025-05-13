#Write a program to print all even numbers up to n
n=int(input('enter an number'))
i=1
while(i<=n):
    if(i%2==0):
      print(i)
    i+=1