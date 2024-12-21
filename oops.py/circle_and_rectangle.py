import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
# circle area = pie * r^2
    def calculate_area(self):
        return math.pi * self.radius**2
# perimenter formiae 2pie*r 
    def calculate_perimenter(self):
        return 2 * math.pi * self.radius
radius = float(input("enter the radius of cirlce"))

circle = Circle(radius)
area = circle.calculate_area()
print("print the area %s" %(area))
perimeter = circle.calculate_perimenter()
print("print the perimeter %s " %(perimeter))





