p=2
while p<1e4:
 if all(p%d for d in range(2,p)):print(p)
 p+=1