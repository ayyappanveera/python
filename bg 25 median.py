n=int(input())
p=[]
p=list(map(int,input().split()))[:n]
s=sorted(p)
m=n//2
print(s[m])
