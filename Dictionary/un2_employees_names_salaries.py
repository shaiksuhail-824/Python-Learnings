##Write a program to enter names of employees and their salaries as input
#  and store them in a dictionary.
'''l=int(input('Enter the lenght '))
d={}
for i in range(1,l+1):
    emp=input('Enter the Employee Name: ')
    sal=int(input('Enter the salary: '))
    d[emp]=sal
print(d)'''
d={}
while True:
    n=input('Enter the name')
    s=int(input('Enter the salary'))
    d[n]=s
    choise=input('enter the you want to enter the more details yes/no')
    if(choise=='no'):
        break
print(d)



