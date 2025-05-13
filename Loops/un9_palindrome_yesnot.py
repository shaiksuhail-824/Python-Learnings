n=int(input('enter the number'))
temp=n
rev=0
while(n>0):
    rev=(rev*10)+n%10
    n=n//10
if(temp==rev):
      print('it is palindrome no')
else:
      print('it is not palindrom no')
#121 171