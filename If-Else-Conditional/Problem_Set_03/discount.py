a=int(input('Enter a number')) 
b=a*100
c=b-(b*10/100)
if(b>1000):
    print('final cost', c )
else:
    print('final cost',b )
