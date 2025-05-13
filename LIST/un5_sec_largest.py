#Write a function to return the second largest number from a list of numbers.
def largest(n): 
    l=[]
    for i in range(0,n):
        element=int(input('Enter the element'))
        l.append(element)
    print(l)
    #l.sort()
    #print(' second largest item is :',l[-2])
    lar=0
    sec=0
    for i in l:
        if(i>lar):
            sec=lar
            lar=i
        elif(i>sec and i!=lar):
            sec=i
    print('second largest value',sec)
x=int(input('enter the length'))
largest(x)