# finding sum of digits by using loop
x=int(input('enter five digit no.'))
sum=0
b=x

for i in range(5):
    a=x%10
    sum=sum+a
    x=int(x/10)

print('sum of digits of %d is='%(b),sum)

