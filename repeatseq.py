pl=int(input())       
ql=list(map(int,input().split()))
i=0
count=1
m=count
r=1
for i in range(pl-1):
    if(ql[i]==ql[i+1]):
        count=count+1
    elif(count>m):
        m=count
        r=count
        count=1
print(r) 
