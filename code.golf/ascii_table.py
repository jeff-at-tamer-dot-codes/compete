print(*['   2 3 4 5 6 7\n','-'*13])
a=48
b=32
for _ in[0]*16:c=[chr(a)+':'];c+=map(chr,range(b,127,16));print(*c+['DEL']*(b>46));a+=1+7*(a==57);b+=1