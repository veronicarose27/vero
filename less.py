l=int(input())
t=list(map(int,input().split()))
p=[]
for i in t:
    if(i<l):
        p.append(i)
y=sorted(p)
print(*y)
