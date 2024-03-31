import sys
for a in sys.argv[1:]:
 a=int(a);b=''
 for c,d in zip([999,899,499,399,99,89,49,39,9,8,4,3,0],'M CM D CD C XC L XL X IX V IV I'.split()):
  while a>c:a-=c+1;b+=d
 print(b)