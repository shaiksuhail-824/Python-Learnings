a=int(input('Enter the number of units'))
b=a*2
c=a*5
if(a<=100):
    print('Free')
elif(a>=100 and  a<=300 ):
    print('the bill:-',b-100*2)
else:
    print('the bill:-',c-100*5-100*6)
