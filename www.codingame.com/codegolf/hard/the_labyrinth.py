I=input
o=''
f=lambda:tuple(map(int,I(o).split()))
H,W,_=f()
t='C?';v='#'
while 1:
 q=[f()];a=[I()for _ in' '*H];d={q[0]:0};r,c=q[0]
 if'C'==a[r][c]:t='T';v='#?'
 while 1:
  r,c=k=q[0];q=q[1:]
  if a[r][c]in t:break
  for w,x,z in[(r-1,c,'UP'),(r+1,c,'DOWN'),(r,c-1,'LEFT'),(r,c+1,'RIGHT')]:
   if-1<w<H and-1<x<W and a[w][x]not in v and(m:=(w,x))not in d:d[m]=k,z+'\n';q+=[m]
 while d[k]:k,o=d[k]