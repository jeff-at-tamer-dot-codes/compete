import sys
for a in sys.argv[1:]:a=a.split();*a,=map(a.index,a);*a,=map(a.count,(0,1,2));print(*[f'{b}{c}'for b,c in zip([+(a[0]<2)]+a,'💎🥇🥈🥉')if b])