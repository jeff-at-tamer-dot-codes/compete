import sys
m=sys.argv[1]
f=m.find
r=f('\n')+1
d={}
q=[e:=f('E')]
while'S'>m[p:=q[0]]:
 q=q[1:]
 for n in[p-r,p-1,p+1,p+r]:
  if(n in d)<1and m[n]in' S':d[n]=p;q+=[n]
while(p:=d.get(p))!=e:m=m[:p]+'.'+m[p+1:]
print(m)