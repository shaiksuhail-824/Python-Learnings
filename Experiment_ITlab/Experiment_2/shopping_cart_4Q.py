n1=str(input('Name of the items1:'))
c1=int(input('Cost of the items1:'))
q1=int(input('Quantity of  items1:'))
print('Total cost of item1=',c1*q1)
total=c1*q1
n2=str(input('Name of the items2:'))
c2=int(input('Cost of the items2:'))
q2=int(input('Quantity of  items2:'))
print('Total cost of item2=',c2*q2)
s=int(input('Shipping charges:'))
total=total+c2*q2
t=total+s
print('Total cost of the two items including the shipping charges is:',t)
if(t>=2000):
   print('Cost afther 10% discount with final amount receipt is:',t-(t*10/100))
else:
       print('The final amount in receipt',t)
