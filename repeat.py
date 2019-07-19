y,z=map(int,input().split())
p=list(map(int,input().split()))
count=0
for i in range(0,len(p)):
    for j in range(1,len(p)):
        if(p[i]==p[j]):
            count=count+1
        if(count==z):
            print(p[i])
        break
    
    
