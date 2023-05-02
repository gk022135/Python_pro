#Read the hours worked and hourly wages of a worker and compute the total wages.
#If the hours worked are more than 40 hours then pay over time at 1.5 times the hourly wages 
#on extra hours
hr_work=float(input('enter hour of work:'))
print('worker are paid 100rs for one hr')

if hr_work>4:
    wages=4*100+(hr_work-4)*1.5*100
    print('toltal wage for',hr_work,'of work is:',wages)
