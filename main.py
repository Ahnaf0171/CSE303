#ex1
a = int(input("Enter A: "))
b = int(input("Enter B: "))

product=a*b

if(product>1000):
    sum=a+b
    print("Sum is = %d" %sum)
else: print("Product is = %d" %product)
#ex2
import math

def circle_rad(r):
    return math.pi*r*r

def circle_peri(r):
    return 2* math.pi*r

r = float (input("Enter radius: "))
area= circle_rad(r)
print("Area of a circle= ", area)

perimeter= circle_peri(r)
print("Perimeter of a circle = ", perimeter)
