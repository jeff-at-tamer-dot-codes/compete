import sys
for c in sys.argv[1:]:
 d={};i=p=0;s=[]
 while i<len(c):
  j=ord(c[i]);v=d.get(p,0);i+=1
  if j<46:d[p]=v+44-j
  elif j<47:print(end=chr(v))
  elif j<63:p+=j-61
  elif j<92:
   s+=[i];q=1
   while q:i+=1;q+=((j:=ord(c[i]))>90)*(92-j)
  elif v:i=s[-1]
  else:s.pop()