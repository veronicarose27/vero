y=int(input())
p=list(map(int,input().split()))
count1=1
count2=1
for i in range(0,y-1):
     if(p[i]<(p[i+1])):
         count1=count1+1
         count2=1
     else:
         for j in range(i+1,y-1):
             if(p[j]<(p[j+1])):
                 count2=count2+1
                 count1=1
         else:
             break
if(count1>count2):
    print(count1)
else:
    print(count2)
    
