T=int(input())
result=[]
for i in range(T):
    values=input().split()
    a,b=values[0],values[1]
    try:
        v=int(a)//int(b)
        result.append(v)  
    except ZeroDivisionError as e :
        result.append("Error Code:"+str(e))
    except ValueError as e:
        result.append("Error Code:"+str(e))
print(result)      
