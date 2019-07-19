y=int(input())
p=list(map(int,input().split()))
u=[]
t=[]
for i in range(0,y):
    if(p[i]%2==0):
        u.append(p[i])
    else:
        t.append(p[i])
if(len(u)==1):
    print(*u)
elif(len(t)==1):
    print(*t)
