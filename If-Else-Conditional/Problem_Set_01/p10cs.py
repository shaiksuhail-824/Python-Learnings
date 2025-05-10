
# v=int(input('enter a number fromzzyyy'))
# if(v==1):
#     print('Sunday')
# elif(v==2):
#     print('Monday')
# elif(v==3):
#     print('Tuesday')
# elif(v==4):
#     print('Wednesday')
# elif(v==5):
#     print('Thursday')
# elif(v==6):
#     print('Friday')
# elif(v==7):
#     print('Saturday')

num1 = int(input("enyer a number"))
if num1 > 0:
    a = num1%10
    b = num1//10
    c = b % 10 
    d = b // 10
    e = d % 10
    f = d // 10
    g = f % 10
    h = f // 10 
    print(a,c,e,g , sep = "")