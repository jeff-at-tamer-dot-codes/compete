from fractions import*
for f in['0/1']+sorted(set(Fraction(n,d)for d in range(51)for n in range(1,d)))+['1/1']:print(f)