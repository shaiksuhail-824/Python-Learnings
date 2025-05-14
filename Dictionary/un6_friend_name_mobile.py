'''
Write a program to input your friends names and their phone numbers and store them in the dictionary as key-value pairs. Perform the following operations on the dictionary:

(a) Display the name and phone number of all your friends

(b) Add a new key-value pair in this dictionary and display the modified dictionary

(c) Delete a particular friend from the dictionary

(d) Modify the phone number of an existing friend

(e) Check if a friend is present in the dictionary or not

(f) Display the dictionary in sorted order of names
'''
v={'suhail':8247793270,'soheb':9897938647,'moin':9838462864,'ashok':9934739428}
print(v.items())
v['goutham']=9847276486
print(v)
del v['suhail']
print(v)
v['soheb']=6305544599
print(v)
print('moin' in v)
print(sorted(v.items()))