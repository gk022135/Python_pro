#Program to accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
a=int(input('enter side1 of triangle:'))
b=int(input('enter side2 of triangle:'))
c=int(input('enter side3 of triangle:'))

if a==b==c:
    print('triangle is EQUILATERAL')
elif a==b!=c or a==c!=b or b==c!=a:
    print('triangle is ISOSCELES')
else:
    print('triange is SCALEN')
