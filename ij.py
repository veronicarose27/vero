l=int(input())
p=list(map(int,input().split()))
count=0
for i in range(0,l):
    for j in range(1,l):
        if(p[i]<p[j]):
            count=count+1
print(count)
