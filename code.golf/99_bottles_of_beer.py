i=99;d=0
while 1:
 b=f' bottle{"s"*(i!=1)} of beer';w=b+' on the wall';print(end=f'{i}{w}.\n\n'*(i!=99)+f'{str(i).capitalize()+w}, {i}{b}.\n'+['Take one down and pass it around, ',f'Go to the store and buy some more, 99{w}.'][d])
 if d:break
 i-=1;d=i<1
 if d:i='no more'