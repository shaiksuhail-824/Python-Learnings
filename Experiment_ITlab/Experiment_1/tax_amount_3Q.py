income=int(input('Enter the income: ' ))
if(income<=300000):
    print('No Tax')
elif(income>=300001 and income<=700000):
    print('The tax amount to be paid to GOI',income*5/100)
elif(income>=700001 and income<=1000000):
    print('The tax amount to be paid to GOI',income*10/100)
elif(income>=1000001 and income<=1200000):
    print('The tax amount to be paid to GOI',income*15/100)
elif(income>=1200001 and income<1500000):
    print('The tax amount to be paid to GOI',income*5/100)
else:
    print('Invalid input')
