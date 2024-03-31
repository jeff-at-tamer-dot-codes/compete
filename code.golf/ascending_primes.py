def f(d,s,a):
 if(s<1)*(a>1)*all(a%q for q in range(2,a)):print(a)
 if s*d<s*10:f(d+1,s-1,a*10+d);f(d+1,s,a)
for i in range(9):f(1,i,0)