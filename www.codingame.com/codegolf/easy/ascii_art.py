w,_,s,*a=open(0)
w=int(w)
for i in a:print(''.join(i[[26,ord(j)-97]['`'<j<'{']*w:][:w]for j in s[:-1].lower()))