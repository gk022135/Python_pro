#Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 
#2 for Monday and so on.
num=int(input('enter a num form 1 to 7: '))
if num==1:
    print('this is SUNDAY')
if num==2:
    print('this is MONDAY')
if num==3:
    print('this is TUESDAY')
if num==4:
    print('this is WEDNESDAY')
if num==5:
    print('this is THRUSDAY')
if num==6:
    print('this is FRIDAY')
if num==7:
    print('this is SATURDAY')

# here using switch case as match 


match num :
    case 1:
       print('this day is SUNDAY')  
    case 2:
        print('this day is MONDAY')
    case 3:
        print('this day is TUESDAY')
    case 2:
        print('this day is WEDNESDAY')
    case 1:
        print('this day is THRUSDAY')
    case 2:
        print('this day is FRIDAY')
    case 1:
        print('this day is SATURDAY')
   