import sys
r=str.replace
a=r('//'.join(b.split()[0]for b in sys.argv[1:]),'/','\n')
b=8
while b:a=r(a,str(b),' '*b);b-=1
b=9812
for c in'KQRBNPkqrbnp':a=r(a,c,chr(b));b+=1
print(a)