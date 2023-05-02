#WAP to accept two numbers and a mathematical operator and perform the operation accordingly.
num1=int(input('enter anumber:'))
num2=int(input('enter number:'))
char=input('enter any operation amoung +,-,*,/,%:-')

if char=='+':
    result=num1+num2
    print(num1,char,num2,'=',result)
elif char=='-':
    result=num1-num2
    print(num1,char,num2,'=',result)
elif char=='*':
    result=num1*num2
    print(num1,char,num2,'=',result)
elif char=='/':
    if num1>num2:
       result=num1/num2
    else:
        result=num2/num1

    print(num1,char,num2,'=',result)
elif char=='%':
    result=num1%num2
    print(num1,char,num2,'=',result)
else :
    print('please enter appopriate choice of give option')