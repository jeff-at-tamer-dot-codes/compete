import sys,fractions as f
for i in sys.argv[1:]:x=f.Fraction(i);print(str(x)+(x==int(x))*'/1')