I=input
c,r=map(int,I().split())
f=lambda x:[I()for _ in' '*x]
a=f(r)
a=[[j[i*c:i*c+c]for j in a]for i in range(20)]
def g():
 b=f(int(I()));n=0
 while b:n=n*20+a.index(b[:r]);b=b[r:]
 return n
x=g();y=g()
z=int(eval(f'{x}{I()}{y}'))
o=[a[0],[]][z>0]
while z:o=a[z%20]+o;z//=20
for i in o:print(i)