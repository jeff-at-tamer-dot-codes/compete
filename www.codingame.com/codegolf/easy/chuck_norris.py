z='0'
a=c=[]
for i in input():
 for j in bin(ord(i)+128)[3:]:
  if j==c:a[-1]+=z
  else:a+=[z*(j<'1')+z,z]
  c=j
print(*a)