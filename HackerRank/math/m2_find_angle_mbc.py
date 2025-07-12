import math
lenght_of_side_AB =int(input())
lenght_of_side_BC =int(input())

lenght_of_side_AC=math.sqrt(lenght_of_side_AB**2+lenght_of_side_BC**2)
lenght_of_side_MC=lenght_of_side_AC/2
print((lenght_of_side_AC))

x=math.atan(lenght_of_side_MC/lenght_of_side_BC)
y=round(math.degrees(x))
print(y)
