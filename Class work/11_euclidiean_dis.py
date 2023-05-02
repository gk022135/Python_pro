# WAP to enter the value of two coordinates and find the Euclidean distance between these 
# two points
x1=int(input('first coordinate x1 '))
y1=int(input('first coordinate y1 '))

x2=int(input('first coordinate x2 '))
y2=int(input('first coordinate y2 '))

a=pow((x1-x2),2)
b=pow((y1-y2),2)

euclidean_dis=pow((a+b),1/2)
print('distance b/w p(%d,%d) to q(%d,%d) ='%(x1,y1,x2,y2),euclidean_dis)