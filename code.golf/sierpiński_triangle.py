k=r,s='▲ ';r=[r]
for i in range(16)[::-1]:print(i*s+s.join(r));r=[k[a==b]for a,b in zip([s]+r,r+[s])]