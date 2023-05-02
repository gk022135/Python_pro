#WAP to check whether the last digit of a number is divisible by 3 or not.
num=int(input('enter a no.:'))
a=num%10

if a%3==0 :
    print('last digit of',num,'is divisible by 3')
else:
    print('last digit of',num,'is NOT divisible by 3')