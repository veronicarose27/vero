p,q=map(int,input().split())
l=list(map(int,input().split()))
o=0
for i in range(0,p):
    for j in range(1,p):
        if(q==l[i]+(l[j])):
            o=1
if o==0:
    print("no")
else:
    print("yes")
        
