import math
integer_a = int(input())
integer_b = int(input())
quotient=math.floor(integer_a/integer_b)
remainder=math.fmod(integer_a,integer_b)
divmod_result=divmod(integer_a,integer_b)
print(quotient)
print(int(remainder))
print(divmod_result)
