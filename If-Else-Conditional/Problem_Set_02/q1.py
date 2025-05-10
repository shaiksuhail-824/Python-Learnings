a=int(input(' Enter the units'))
b=a*5
c=a*10
if(a<=100):
    print('price:-Nocharge')
elif( a>=100 and  a<=200):
    print(b-100*5)
else:
    print(c-100*10-100*5)
 