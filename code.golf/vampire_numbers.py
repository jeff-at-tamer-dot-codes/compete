a=set();s=sorted
for i in(r:=range(1,999)):
 for j in r:a.add((s(f'{i}{j}')==s(str(i*j)))*(i%10+j%10>0)*i*j)
for k in(a:=s(a))[6:9]+a[10:13]+[6880]+a[67:]:print(k)