#to find the roots of a quadratic equation
import math
print('ax²+bx+c: roots of equation find')
print('enter cofficients of x² ,x,c')

input('enter quadractic eqn:-')

a=int(input('enter coefficient of x² '))
b=int(input('enter cofficient of x '))
c=int(input('enter constant term '))

d=pow(b,2)
e=d-4*a*c   # d=b²-4ac
print('d =',e)

D1=pow((e),1/2)  # D1=sqrt(d)
print('D1 =',D1)
if e>0:
    print('roots are different and real')
    x1=(-b-D1)/(2*a)
    x2=(-b+D1)/(2*a)
    print('roots are =',x1,x2)
elif e==0:
    print('rooot are same')
    x=(-b+D1)/(2*a)
    print('root = ',x)
else :
    print('root does not exist')
