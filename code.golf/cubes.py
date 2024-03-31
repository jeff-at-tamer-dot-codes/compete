p=print;a,b,c,d,e,f=' █─╱│\n'
for i in range(1,8):
 g=b+c*i*4+b;h=f+e+a*i*4+e+a*i;r=range(i);p(a*i+a+g)
 for j in r:p(a*(i-j)+d+a*i*4+d+a*j+e)
 p(g+a*i+e+(h+e)*(i-1)+h+b)
 for j in r:p(h[1:-j-1]+d)
 p(g+f)