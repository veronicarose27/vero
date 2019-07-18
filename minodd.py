p=int(input())
l=[]
if(p%2!=0):
    print("1")
else:
    for i in range(1,p):
        if(p%i==0 and i%2!=0):
            u=p//i
            l.append(u)
print(min(l))
        
