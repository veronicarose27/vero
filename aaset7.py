p,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,p):
    for j in range(1,p):
        sum=l[i]+(l[j])
        if(sum==q):
            print("yes")
    break
else:
    print("no")
