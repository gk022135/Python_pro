# WAP to enter the marks of a student in 5 different subjects and find his/her average marks
sum=0
for i in range(1,6):
    a=int(input('enter mark of subject%d '%(i)))
    sum=sum+a

avg=sum/5
print('average marks of five subject=',avg)