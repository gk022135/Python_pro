# WAP to find the cost of filling a cylindrical vessel with milk, if the cost of milk is 40rs /litre
import math
print('enter data in metre')
R=int(input('enter radius of cylinder base '))
h=int(input('enter height of cylinder '))

volume_cylinder=3.14*R*R*h
print('volume of cylinder =',volume_cylinder)

print('the cost of milk is 40rs /litre')
cost_filling=volume_cylinder*40

print('total cost for filling milk to %f m cube volume='%(volume_cylinder),cost_filling)