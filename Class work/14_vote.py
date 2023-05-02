#WAP to check whether a person is eligible to vote or not.
citizenship=input('enter nation(in capital letter):')
age=int(input('enter person age:'))

if citizenship=='INDIAN' and age>=18 :
    print('the  person age of %d is citizen of of %s is eligible for voting.'%(age,citizenship))
else :
    print('the  person age of %d is citizen of of %s is NOT eligible for voting.'%(age,citizenship))
