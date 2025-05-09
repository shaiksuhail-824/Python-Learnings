s=str(input('Enter the sentance: '))
s1=s.split()
for w in s1:
      a=0
      d=0
      for i in w:
          if(i.isalpha()):
                a=a+1
          elif(i.isdigit()):
                 d=d+1
      if(a!=0 and d!=0):
            print(w,end=' ')
s3=''
for w in s1:
      if(w.isalnum()):
            s3=s3+w
print(s3)

 