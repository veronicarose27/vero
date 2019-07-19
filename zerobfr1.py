k=int(input())
a1=(input())
b=""
c=""
for i in range(len(a1)):
    if a1[i]=="1":
        b=b+a1[i]+" "
    elif a1[i]=="0":
        c=c+b
        b=""
print(c.strip())
