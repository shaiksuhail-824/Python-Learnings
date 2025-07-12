N_and_X = input().split()
l=[]
for i in range(int(N_and_X[1])) :
     subject = list(map(float,input().split()))
     l.append(subject)
print(l)
x = []
for i in l :
    x = x + [i]
score_obtained_all_subject = list(zip(*x))
for i in score_obtained_all_subject :
     average = sum(i)/int(N_and_X[0])
     print(average)