def LCM(n):
    a=[]
    n1=1
    for i in range(n):
          ele=int(input('ENter the element'))
          a.append(ele)
          print(a)
          for j in range(1,(n1*ele)+1):
               if(j%n1==0 and j%ele==0):
                    n1=j
                    
                    print('Lcm of Entered list is :',j)
                    break
x=int(input('Enter the range'))
LCM(x)
