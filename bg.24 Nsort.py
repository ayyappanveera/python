    
l=int(input())
o=(int(i) for i in input().split())
g=sorted(o)
i=0
while i<l:
  print(g[i],"",end="")
  i+=1
