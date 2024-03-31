i=0
while i<1e3:i+=1;print('Foo'*(i%2<1)+'Fizz'*(i%3<1)+'Buzz'*(i%5<1)+'Bar'*(i%7<1)or i)