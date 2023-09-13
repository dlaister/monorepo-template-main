"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

"""
Needed for creating an abstract base class per python documentation: https://docs.python.org/3/library/abc.html
"""
from abc import ABC, abstractmethod

"""
Task 2.3 - Create an abstract Shape class with rectangle as the a sub class.
Should contain a set_values and area method.
"""
class Shape(ABC):
    # in class a lambda was used - not sure why.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def set_values(self, width, height):
        pass

    @abstractmethod
    def area(self):
        pass

"""
Rectangle needed to be made a sub class that inherits shape.
Class correctly changed to allow for runtime.
"""
class Rectangle(Shape):
    #changed x,y to w,h to be more in line with what they represent (width, height)
    def set_values(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    # Create a rectangle object
    # tested functionality by creating a different rect object
    rect = Rectangle(1,1)
    rect1 = Rectangle(1, 1)
    rect2 = Rectangle(1, 1)
    rect3 = Rectangle(1, 1)
    rect4 = Rectangle(1, 1)


    # Call a member function
    # tested functionality with different w,h values to see if expected was a match with actual
    rect.set_values(1, 1)
    rect1.set_values(2, 2)
    rect2.set_values(3, 4)
    rect3.set_values(4, 5)
    rect4.set_values(10, 10)


    # Print out the area function
    print("area:", rect.area())
    print("area:", rect1.area())
    print("area:", rect2.area())
    print("area:", rect3.area())
    print("area:", rect4.area())

