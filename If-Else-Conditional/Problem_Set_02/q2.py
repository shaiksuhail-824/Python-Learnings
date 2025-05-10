a=int(input(' Enter the Bike price'))
if(a>100000):
    print('the road tax to be paid :-', a*(15/100))
elif(a>50000 and a<=100000):
    print('The road tax to be paid :-' ,a*(10/100))
elif(a<=50000):
    print('The road tax to be paid :-' ,a*(5/100))
