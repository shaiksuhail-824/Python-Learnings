a=int(input('Enter the Km:'))
b=str(input('Enter the range'))
if(a>=100 and b=='outstanding'):
    print('total amount Rs.',(a-6)*10+100)
elif(a<=100 and b=='rural'):
    print('total amount Rs.',(a-6)*20+100)
else:
    print('total amount Rs.100')
