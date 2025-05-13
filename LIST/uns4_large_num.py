def largest(n):
    l=[]
    for i in range(0,n):
        element=int(input('Enter the element'))
        l.append(element)
    print(l)
    #print('largest item is',max(l))
    lar=l[0]
    for i in l:
        if(i>lar):
            lar=i
    print('largest item is :',lar)
x=int(input('enter the length'))
largest(x)