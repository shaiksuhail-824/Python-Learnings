'''
Create a dictionary ODD of odd numbers between 1 and 10, where the key is the decimal number and the value is the corresponding number in words. Perform the following operations on this dictionary:

(a) Display the keys

(b) Display the values

(c) Display the items

(d) Find the length of the dictionary

(e) Check if 7 is present or not

(f) Check if 2 is present or not

(g) Retrieve the value corresponding to the key 9

(h) Delete the item from the dictionary corresponding to the key 9
'''
odd={1:'one',3:'three',5:'free',7:'seven',9:'nine'}
print(odd)
print(odd.keys())
print(odd.values())
print(odd.items())
print(len(odd))
print(7 in odd)
print(2 in odd)
odd[9]="NINE"
print(odd)
odd.pop(9)
print(odd)