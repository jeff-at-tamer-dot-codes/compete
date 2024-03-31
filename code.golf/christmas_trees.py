*r,=range(10)
for i in r[3:]:
 for j in r[:i]+[0]:print(' '*(i-j)+'*'*(j*2+1))
 print()