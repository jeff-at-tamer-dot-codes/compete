import fractions as F
q=lambda i,j:F.Fraction(i,j)if j else''
m=lambda x,y:[tuple(sorted(i+j))for i in x for j in y]
f=lambda x,y:[z:={},[z.setdefault(k,set()).update(m(x[i],y[j]))for i in x for j in y for k in[i+j,i-j,j-i,i*j,q(i,j),q(j,i)]if''!=k]][0]
for i in sorted(f(b:=f(a:={i:{(i,)}for i in range(1,14)},a),b)[24]|f(a,f(a,b))[24]):print(*i)