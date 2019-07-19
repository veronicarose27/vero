p,q=map(str,input().split())
count=0
for i in p:
    for j in q:
        if(i==j):
            count=1
if(count==1):
    print("yes")
else:
    print("no")
            
