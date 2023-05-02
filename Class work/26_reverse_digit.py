#A five-digit number is entered through the keyboard. 
#Write the code to obtain the reversed number and determine whether it is a palindrome or not.
num=int(input('enter a five digit no.:'))
sum=0
a=num%10
b=int(num/10)
sum=sum+a*10000

a=b%10
b=int(b/10)
sum=sum+a*1000

a=b%10
b=int(b/10)
sum=sum+a*100

a=b%10
b=int(b/10)
sum=sum+a*10

a=b%10
sum=sum+a
print('reverse of number',num,'=',sum)

if num==sum:
    print(num,'is palindrome number')