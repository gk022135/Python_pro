#Any number is entered through the keyboard, write the code to determine 
#whether the number is one digit,two digit, three digit, or more than three digit number
num=int(input('enter any number:'))
a=num
for i in range(num):
    a=int(a/10)
    if a==0:
        print('number of digits are:',i+1)
        break
