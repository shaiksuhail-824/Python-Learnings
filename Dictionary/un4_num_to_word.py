#Write a program to convert a number entered by the user into its corresponding number in words. 
#For example, if the input is 876 then the output should be 'Eight Seven Six'.
d={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
n=input('Enter the number')
for i in n:
    print(d[i] ,end=' ')