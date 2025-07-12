import math
integer_a = float(input())
integer_b = float(input())
integer_m = float(input())
result_1 = math.pow(integer_a,integer_b)
result_2 = math.fmod(result_1,integer_m)
print(int(result_1))
print(int(result_2))
