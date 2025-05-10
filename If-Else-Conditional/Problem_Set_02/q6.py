a=int(input('Enter the Kilometer covered'))
if(a<=10):
    print('the bill:-' ,a*11)
elif(a>=10 and a<=90):
    print('the bill:-' ,(a-10)*10+110 )
else:
    print('the bill:-',(a-100)*9+1010)