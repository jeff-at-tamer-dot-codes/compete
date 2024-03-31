import sys
s=str.split
for a in sys.argv[1:]:
 b,*d=s(a,'\n');b,c=map(int,s(b));e=0
 for z in d:
  i=s(z)
  while i:
   j=[];k=m=0
   while i and m+len(j)+len(i[0])<=c:m+=len(i[0]);j+=[i.pop(0)]
   while i and m<c:j[k]+=' ';k=(k+1)%(len(j)-1);m+=1
   print(' '*b+' '[:i==[]].join(j));b-=e;c+=e+e;e=1-e
  print();b-=e;c+=e+e;e=1-e