#Write a program to find no_ words, no_letters, no_digits and no_blanks in a line?
s=str(input('Enter the sentence '))
a=0
b=0
c=0

for i in s:
    if(i.isalpha()):
       a=a+1
    elif(i.isdigit()):
        b=b+1
    elif(i.isspace()):
        c=c+1   
print('alphabet:',a,'digit;',b,'space',c,'word',c+1)


