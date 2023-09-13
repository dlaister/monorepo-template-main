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
"""
class Rectangle(Shape):
    """
    Task 2.1 - Added constructor with PRIVATE variables, width and height.
    """
    # in class a lambda was used - not sure why.
    def __init__(self, width, height):
        self.__set_width = width
        self.__set_height = height

    """
    Task 2.2 - Added getter for PRIVATE variable, width.
    """
    def get_width(self):
        return self.__set_width

    """
    Task 2.2 - Added getter for PRIVATE variable, height.
    """
    def get_height(self):
        return self.__set_height

    def set_values(self, x, y):
        self.width = x
        self.height = y

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
