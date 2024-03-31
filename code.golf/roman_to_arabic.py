import sys
d={'':0};a='I';s=1
for b,c in'VX LC DM ..'.split():
 for i in set(d):
  for j in range(5):d[e:=a*j+i]=s*j+d[i];d[b+e]=s*5+d[e]
  d[a+b+i]=d[e];d[a+c+i]=d[b+e]
 a=c;s*=10
for a in sys.argv[1:]:print(d[a])