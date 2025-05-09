kilo=int(input('enter the kilometets' ))
station=str(input('Enter rural/outstation' ))
if(kilo<=6):
    print('Total amount:100')
elif(kilo<=100 and station=='rural'):
    print((20*(kilo-6))+100)
elif(kilo>100 and station=='outstation'):
    print((10*(kilo-6))+100)
else:
    print('invalid output')

    
