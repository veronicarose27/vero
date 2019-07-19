y,z=map(int,input().split())
p=list(map(int,input().split()[:y]))
q=list(map(int,input().split()[:z]))
l=p+q
x=sorted(l)
print(*x)
