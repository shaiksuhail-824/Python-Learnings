f=open('mytext.txt','w')
n=5
for i in range(1,n+1):
    for j in range((n-i)*2):
        f.write(' ')
    for j in range((2*i)-1):
        f.write(str(j+1)+" ")
    f.write('\n')
f.close()