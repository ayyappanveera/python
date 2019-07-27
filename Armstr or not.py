a=int(input())  
s=0  
t=a
while t>0:  
       d=t% 10  
       s+= d**3  
       t//= 10        
if a==s:
  print("yes")  
else:  
  print("no")   
