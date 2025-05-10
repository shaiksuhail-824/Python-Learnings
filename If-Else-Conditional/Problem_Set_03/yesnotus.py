a=int(input("Enter the numberof class held"))
b=int(input("Enter  the number of you attend "))
m=str(input('you have medical cause?? if yes=y or no=n :-'))
p=(b/a)*100
if(m=='y'):
    print('you can sit there')
    
else:
    if(p>=75):
      print(' You are allowed to write the exam')
      print('your Percentage is:',p)
    else:
     print('you are  not allowed to write the exam')
     print('Your percentage is:',p)