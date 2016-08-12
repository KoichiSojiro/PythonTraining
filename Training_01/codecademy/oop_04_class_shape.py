'''
Created on Jul 25, 2016

@author: trannh08
'''
class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
    def detail(self):
        print("I'm a Shape with " + str(self.number_of_sides) + " sides.")

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def detail(self):
        print("I'm a Triangle with measurement of 3 sides are: " + str(self.side1) + ", " + str(self.side2) + ", " + str(self.side3) + ".")

my_shape = Shape(5)
my_shape.detail()

my_triangle = Triangle(3, 4, 5)
my_triangle.detail()