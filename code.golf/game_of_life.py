import sys
_,a=sys.argv
r=a.find('\n')
for i,j in enumerate(a):s=sum(len(a)>n>=0and'#'==a[n]for m in[1,r,r+1,r+2]for n in[i-m,i+m]);print(end=[j,'.#'[s==3or 1<s<4and'.'>j]][j>' '])