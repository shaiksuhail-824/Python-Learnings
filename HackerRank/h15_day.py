import calendar
N=input("enter the date in  mm,dd yyyy format ")
month,day,year=map(int,N.split())
x=calendar.weekday(year, month, day)
print(calendar.day_name[x])
