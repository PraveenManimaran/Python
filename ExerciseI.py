'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise I
'''
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return math.pi * math.pow(self.radius,2)
    
    
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
    def getVolume(self):
        return super().getArea()* self.height


c1 = Circle(4)
print(f'Circle area is: {c1.getArea():.2f}')

c2 = Cylinder(2,5)
print(f'Cylinder volume is: {c2.getVolume():.2f}')



'''

Execution results:

Circle area is: 50.27
Cylinder volume is: 62.83

'''   