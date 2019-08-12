h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
if(h1<=24 and m1<=60):
    if(h2<=24 and m2<=60):
        hr=abs(h1-h2)
        min=abs(m1-m2)
print(hr,min)
