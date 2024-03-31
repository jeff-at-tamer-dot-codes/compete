for i in(r:=range(1,1001)):
 if sum(j*(i%j<1)for j in r)>i+i:print(i)