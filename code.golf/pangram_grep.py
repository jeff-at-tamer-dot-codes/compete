import sys
for a in sys.argv[1:]:
 if sum('`'<c<'{'for c in set(a.lower()))==26:print(a)