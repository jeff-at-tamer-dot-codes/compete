import sys
for i in sys.argv[1:]:a,b,c,d,e,f,g,h=map(int,i.split());c+=a;d+=b;g+=e;h+=f;print((a<g)*(b<h)*(e<c)*(f<d)*(min(c,g)-max(a,e))*(min(d,h)-max(b,f)))