a=int(input('Enter a number'))
b=int(input('Enter a number'))
c=int(input('Enter a number'))
if(13<=a<=14 or 16<=a<=19 and 13<=b<=14 or 16<=b<=19  and  13<=c<=14 or 16<=c<=19  ):
    print(0)
elif(13<=a<=14 or 16<=a<=19  and 13<=c<=14 or 16<=c<=19 ):
   print(b)
elif(13<=a<=14 or 16<=a<=19  and 13<=b<=14 or 16<=b<=19 ):
   print(c)
elif(13<=b<=14 or 16<=b<=19  and 13<=c<=14 or 16<=c<=19 ):
   print(a)
elif(13<=a<=14 and 16<=a<=19):
   print(b+c)
elif(13<=b<=14 and 16<=b<=19):
   print(a+c)
elif(13<=c<=14 and 16<=c<=19):
   print(b+a)
else:
   print(a+b+c)