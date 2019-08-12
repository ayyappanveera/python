p=int(input())
a=list(map(int,input().split()))[:p]
c=0
for i in range(p):
    c+=a[i]
d=c//p
print(d)
