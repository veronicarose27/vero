p=int(input())
l=list(map(int,input().split()[:p]))
m=list(map(int,input().split()[:p]))
for i in l:
    for j in m:
        if(i==j):
            print(i,end=" ")
