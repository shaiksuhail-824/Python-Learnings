a=int(input('Enter your age'))
b=str(input('Enter your gender'))
c=str(input('Enter yout martial status'))
if(b=='f'):
      print('you will work only in urban area')
elif(b=='m'and a<=40 and a>=20):
   
      print('You may Work any where')
elif(b=='m' and a<=60 and a>=40):
   
      print('you will work only in urban area')
else:
   print('ERROR')
