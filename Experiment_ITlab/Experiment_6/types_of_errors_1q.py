#types of error ---5marks
l=[10,20,30,40]
l.append(50)
#l.appen(50)#attribute error
print(l)

#from fractions import Fraction
   #  f=Fraction(8,2)#attribute error
#print(f.numerator)
from math import sqrt
#from math import squareroot ---importerror
print(sqrt(4))
l=[1,2,10,5,7]
print(l[2])
#print(l[12]) #--indexerror.out of range
d={1:'rkv',2:'ong',4:'ssn'}
print(d[2])
#print(d[3]) #---keyerror
#print(rkv) --nameerror
a=10
b='rkv'
#print(a+b)#---typeerror
print(f'{a}{b}')
print(int(8))
#print(int('ssn')) #--value error
a=10
b=0
print(a/b) # ---zero error