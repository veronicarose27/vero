y=int(input())
p=list(map(int,input().split()[:y]))
l=sorted(p)
u=len(l)
k=l[u-1]-l[0]
print(k)
