f=open('/home/shaik-suhail/Documents/P2S2/python/Experiment_ITlab/Experiment_6/Mydocument.txt','r')
f.seek(0)
x=f.read()
d=v=c=uc=lc=r=0
vowels='aeiouAEIOU'
for i in x:
    if(i.isalpha()):
        if(i in vowels):
            v=v+1
        if(i not in vowels):
            c=c+1
        if(i.isupper()):
            uc=uc+1
        if(i.islower()):
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    elif(not i.isspace()):
        r=r+1
print('Digits:',d)
print('Vowels',v)

print('consonants',c)

print('Uppercase',uc)

print('Lowercase',lc)

print('Other than letters and digits',r)
f.close()

