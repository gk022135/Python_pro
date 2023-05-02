# finding factorial of a no.
num=int(input('enter a positive no.'))
product=1
for i in range(1,num+1):
    product=product*i

print('factorial of', num,'=',product)