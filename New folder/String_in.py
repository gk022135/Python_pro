# string start
# string is written in flowing waya
# 01 by single quotes' '
# 02 by double quotes " "
# 03 by tripple quotes ''' '''

a='madharchod'
b="bsdk"
c=''' chal phad de'''
print(a)
print(b)
print(c)

#string slicing that mean a particular letter secleting from whole word/string
name='madharchod'
# name[index of particular letter]
name[0]
print(name[0])

# slicing more letter name[x:y] where x and y are index
print(name[2:8])
# slicing like some letter skip [x:y:z] x,y,z index 
# here value printed x to y such that interval b/w  x & y is equal to z
print(name[0:4:2])

# len("string name ")=gives length of string
print(len(name))
print(len("madharchod"))
print(len("anystring"))

# name of string.endswith("xyz")=give that string end with xyz or not by output true or false
print(name.endswith("chod"))

#name of string.count("x")=give occurence of x in selected string
print("no.of h in madharchod")
print(name.count("h"))
print("no.of a in madharchod")
print(name.count(a))

# string.capitalize()=captlaize first letter of string
print(name.capitalize())

#string.find(write word which you find)=give index of first occurence of that word
print(name.find("mad"))

#string.replace("old word","new word")
name=name.replace("mad","cha")
print(name)
#or
print(name.replace("cha","mad"))