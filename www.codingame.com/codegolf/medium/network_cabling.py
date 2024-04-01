I=input
a=[int(i)for _ in' '*int(I())for i in I().split()]
y=sorted(a[1::2])
I(max(x:=a[::2])-min(x)+sum(abs(i-y[len(y)//2])for i in y))