# program for finding sum of factorial
n=int(input('enter no.whoose fact sum find '))
sum=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum=sum+fact
    
print('%d!=%d'%(n,fact))   #string formating
print('sum of ',n,'!=',sum)
print('sum of %d!=%d'%(n,sum))