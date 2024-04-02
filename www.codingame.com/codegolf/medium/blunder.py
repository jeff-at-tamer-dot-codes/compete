*a,=open(0)
b=r=z=0
t=[]
while a[r:]:t+=[(r,c)for c in range(99)if'T'==a[r][c:c+1]];r+=1
r=0
while(c:=a[r].find('@'))<0:r+=1
d=(('SOUTH',1,0),('EAST',0,1),('NORTH',-1,0),('WEST',0,-1))
l=[]
s={}
*a,=map(list,a)
while'$'!=(j:=a[r][c]):
 if(k:=(r,c,b,z,d))in s:l=0;break
 s[k]=1
 if'W'<j:a[r][c]=' ';s={}
 if'B'==j:b=~b
 if'I'==j:d=d[::-1];z=3-z
 if'T'==j:r,c=t[t[0]==(r,c)]
 if y:=[i for i in[0,1,2,3]if d[i][0][0]==j]:[z]=y
 for q in[z,0,1,2,3]:
  v,w,x=d[q];j=a[r+w][c+x]
  if('#'!=j)*(j<'X'or b):break
 l+=[v];r+=w;c+=x;z=q
print('\n'.join(l)if l else'LOOP')