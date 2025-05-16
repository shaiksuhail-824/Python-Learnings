user_input=int(input('Enter the number'))
print('Step-1 Multlipy by 16')
print('Step-2 Add 144 to the  number')
print('Step-3 Divide by 16 to the number')

operation=(user_input*16+144)/16
print(operation)
guess_num=operation-9
print('your guessed number is ',guess_num)

