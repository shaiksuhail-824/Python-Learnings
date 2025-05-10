a=int(input(' Enter the units'))
if(a<=100):
    print('price:-Nocharge')
elif( a>=100 and  a<=200):
    print((a-100)*5)
else:
    print((a-200)*10+500)
