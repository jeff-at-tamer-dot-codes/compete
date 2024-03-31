i=1
while i<1e4:
 f=[d for d in range(1,i+1)if i%d<1]
 if sum(f)%len(f)<1:print(i)
 i+=1