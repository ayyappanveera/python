c,k=map(int,input().split())
a=k
s=0
arr=[]
arr =list(map(int,input().strip().split()))[:c]
for i in range(0,a):
  s=s+arr[i]
print(s)
