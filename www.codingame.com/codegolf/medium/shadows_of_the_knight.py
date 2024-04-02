I=input
f=lambda:map(int,I().split())
a=b=0
w,h=f()
I()
x,y=f()
while d:=I():
 if'E'>d:b=y
 if'T'<d:h=y
 if'L'in d:w=x
 if'R'in d:a=x
 print(x:=(a+w)//2,y:=(b+h)//2)