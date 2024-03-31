import sys,collections as c
c=c.Counter;K=' of a Kind';S='Straight';F='Flush'
*m,=range(-1,12)
m[1]=13
for a in sys.argv[1:]:
 *b,=map(ord,a);f=len(c(x>>4&3for x in b))-1;s=max(q:=c(p:=[(m+[11,12])[x%16]for x in b]))-(z:=min(q))-4and max(r:=c(x%13for x in p))-min(r)-4or len(q)-5;j=c(q.values())
 print('Four'+K if j[4]else['Three'+K,'Full House'][j[2]]if j[3]else'Two '*(j[2]-1)+'Pair'if j[2]else'High Card'if s*f else[S,F][f<1]if s|f else[S,'Royal'][z>8]+' '+F)