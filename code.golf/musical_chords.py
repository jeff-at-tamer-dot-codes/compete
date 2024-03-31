import sys
g=lambda m,x,y,f:(f(*b)-f(*a)-x)%m<(f(*c)-f(*b)-y)%m<2
for t in sys.argv[1:]:
 a,b,c=sorted(t.split())
 for i in range(12):
  if g(7,2,1,lambda*z:ord(z[0]))*g(12,i//2%2+3,i%2+2,lambda p,q='.':ord(q)+'.A.BC.D.EF'.find(p)):print(a+'°m +'[i%4])
  a,b,c=b,c,a