a=str(input('which type  popcorn would you want??'))
if(a=='salted'):
    print('amount with GST:-',20+(5/100)*20)
elif(a=='packaged'):
    print('amount with GST:-',40+(12/100)*40)
else:
    print('amount with GST:-',150+(18/100)*150)