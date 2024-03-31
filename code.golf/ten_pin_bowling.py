import sys
for a in sys.argv[1:]:
 s=l=0;b=[]
 for i in(a:=[ord(c)%59for c in(a.rstrip()+'-')[:30]if' '<c]):b+=[l:=[10*(i==29),[10-l,i-48][48<i]][46<i]];s+=l
 print(s+sum(j*(i==47)+(j+k)*(i==29)for i,j,k in zip(a[:-3],b[1:],b[2:])))