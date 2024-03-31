#include <stdio.h>
int main(){for(int i=1;i<=100;++i)printf(i%15?i%5?i%3?"%d\n":"Fizz\n":"Buzz\n":"FizzBuzz\n",i);}