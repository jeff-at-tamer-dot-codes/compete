a,b,c,d=map(int,input().split())
while input():x=a>=c;y=b>=d;print(['N'[y:],'S'][b>d]+['W'[x:],'E'][a>c]);a-=a>c or x-1;b-=b>d or y-1