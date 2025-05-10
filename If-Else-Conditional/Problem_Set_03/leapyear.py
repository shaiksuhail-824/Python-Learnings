a=int(input('Enter the year'))
if(a%4==0 and a%100!=0 or a%400==0):
    print( 'it is leap year')
else:
    print('it is not leap year')