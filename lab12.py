import math

class Vector:

    # constructor. Takes 3 args: self,x,y. Default for both x and y is 0. No return
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # for printing. Takes 1 arg: self. Returns a string (precise to 2 decimals).
    def __str__(self):
        return str(round(self.x, 2)) + " " + str(round(self.y, 2))

    # for displaying in the shell. Takes 1 arg: self. Returns a string
    def __repr__(self):
        return str(round(self.x, 2)) + " " + str(round(self.y, 2))

    # vector + vector. Takes 2 args: self and a vector. Returns a new vector
    def __add__(self, z):
        return Vector(self.x + z.x, self.y + z.y)

    # vector – vector. Takes 2 args: self and a vector. Returns a new vector
    def __sub__(self, z):
        return Vector(self.x - z.x, self.y - z.y)

    # possibilities: vector*float or float*vector (scalar product) or vector*vector (dot product).
    # Get it to do just one of the product’s first, then use introspection to do both
    def __mul__(self, z):
        if type(z) == Vector:
            return (self.x * z.x) + (self.y * z.y)
        return Vector(self.x * z.x, self.y * z.y)
    def __rmul__(self, z):
        return (self.x * z.x) + (self.y * z.y)

    # vector == vector. Takes 2 args: self and a vector. Returns True or False.
    def __eq__(self, z):
         if self.x == z.x and self.y == z.y:
             return True
         return False

    # magnitude of the vector. Takes 1 arg, self. Returns a float
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # conversion to a unit vector. Takes 1 arg, self. Scales the vector by the inverse of
    # the magnitude (1/magnitude). No return value. Raises ValueError if magnitude is 0
    # with message “Cannot convert zero vector to a unit vector”
    def unit(self):
        unit = 1 / self.magnitude()
        if unit == ValueError:
            print('Cannot convert zero vector to a unit vector')
        return unit