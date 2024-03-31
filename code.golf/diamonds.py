*r,=map(int,s:='123456789')
f=lambda a,x:a[:x-1]+a[:x][::-1]
for i in r:
 for j in f(r,i):print(' '*(10-j)+f(s,j))
 print()