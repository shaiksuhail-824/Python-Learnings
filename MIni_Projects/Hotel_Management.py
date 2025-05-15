print('Fasa Hotel Menu')
print(' Dosa:40Rs \n Idly:30Rs \n Poori:35Rs \n Voda:20Rs \n Upma:30 ' )
menu={'dosa':40 , 'idly':30 , 'poori':35 ,'voda':20 , 'upma':30}
amount=0
item1=str(input('Enter an item you want! '))
if item1 in menu:
    amount=amount+menu[item1]
    print(f'you order the {item1}, it is listed in order')
else:
    print('you entered {item1}  curently not available ')
user=str(input('you will order some more items?? (Yes/No)'))
if user=="yes":
   item2=str(input('Enter a item you want! '))
   if item2 in menu:
       amount=amount+menu[item2]
       print(f'you ordered thr{item2}')
   else:
       print(f'you entered {item2} not available')
print(f'you will be pay  amount: {amount}')   
print('Thank you  visit again....!!')