import math

# Base class - Shape
class Shape:
    def area(self):
        """
        Base method to calculate area. 
        This method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override this method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle (length × width).
        """
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize a Circle instance with radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)
