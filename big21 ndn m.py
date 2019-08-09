def str(a,d,n):
  str=(n/2)*(2*a+(n-1)*d)
  return str
n,a,d=map(int,input().split())
print(int(str(a,d,n)))  
