import sys
for i in sys.argv[1:]:
 j=0;k=10
 for c in i:
  if'-'<c:j-=k*int(c);k-=1
 j%=11;print(i+['X',str(j)][j<10])