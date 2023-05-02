"formate of string is use put data like float,integer,char in a string"
 
name=input("enter your name\t")
address=input("address\t")
age=input("enter age")
study=input("currently studied at")
fee=200000
value=44.89

biodata='''hello i am %s from %s my age is %s.currently pursuing %s in cse from 
shri mata vaishno devi university paid %d random 
float value %4.2f'''%(name,address,age,study,fee,value)

print(biodata)
