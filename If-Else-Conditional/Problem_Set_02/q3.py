a=int(input('Enter a your salary'))
b=int(input('Enter year of service'))
if(a<10):
    print('The net bonus amount:-',a*10/100)
elif(a>=6 and a<=10):
    print('The net bonus amount:-',a*8/100)
elif(a>6):
    print('The net bonus amount:-',a*5/100)
    
    