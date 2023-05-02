# list is collection of data 
#list can be changable

list1=[12,23,'gaurav','G',7.99,'Gkk']

#acessing elements of list
print(list1[2])
print(list1[5])
print(list1[1:4])
print(list1[0:3:5])

list1[2]='gauravkumar'
list1[4]='hello'
print(list1)

list1.append(9)
list1.append(123)
print(list1)

del list1[6]
del list1[2]
print(list1)

list1.reverse()
print(list1)


list1.insert(12,21)
print(list1)

list1.insert(2,23)
list1.remove(23)
print(list1)
