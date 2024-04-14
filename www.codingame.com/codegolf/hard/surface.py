I=input;I()
a=[[[0]*(c<'C')for c in I()+' ']for _ in' '*int(I())]+[I()*9999]
while 1:
 *q,=map(int,I().split());X,Y=q;i=0
 while i<len(q):
  x,y=q[i:i+2]
  if a[y][x]:q[i:i+2]=[]
  else:a[y][x]=q;q+=[x-1,y,x,y-1,x,y+1,x+1,y];i+=2
 print(len(a[Y][X])>>1)