import sys
for a in sys.argv[1:]:
 s=max(a:=a.split('\n'))
 for c in a[-1][1:-1]:s=[i for i in a if i[2:3]==s[a[0].find(c)]][0]
 print(s[2:4]+['Reject','Accept'][s[1]>' '])