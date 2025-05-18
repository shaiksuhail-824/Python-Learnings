def is_leap(year):
    leap = False
    
    if(year%4 and year%100 or year%400):
       leap=True
    return leap

year = int(input())
print(is_leap(year))
def is_leap(year):
    if(year%4 and year%100 or year%400):
       leap=True
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))