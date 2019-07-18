ni=int(input())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
al=set(al)
bl=set(bl)
if(al & bl):
  c=sorted(al&bl)
  print(*c,sep=' ')
