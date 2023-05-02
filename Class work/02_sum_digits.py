# findimg sum of five digits number
x=int(input("please enter five digit no."))
sum=0

b=x%10
sum=sum+b
a=int(x/10)

b=a%10
sum=sum+b
c=int(a/10)

d=int(c/10)
b=c%10
sum=sum+b

e=int(d/10)
b=d%10
sum=sum+b

f=int(e/10)
b=e%10
sum=sum+b

print(a,c,d,e,f,b)
print('sum of five digits=',sum)