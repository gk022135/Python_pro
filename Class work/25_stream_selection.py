#Accept the marks of English, Math and Science, Social Studies and display the stream allotted
#according to the following:
eng=int(input('enter marks of emglish='))
math=int(input('enter marks of maths='))
sci=int(input('enter marks of science='))
s_s=int(input('enter marks of s.s='))

if math>=80 and sci>=80 :
      if s_s>=80 and eng>=80:
         print('student is eligible for science stream')
elif eng>=80 and sci>=50 :
    print('student is best for commerce')
elif eng>=80 and s_s>=80 :
    print('student is best for Humanity')
