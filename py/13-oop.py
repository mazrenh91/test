# inheritance
class Shape:    # parent class
    def __init__(self, name):
        self.name = name    # common attribute

    def area(self): # common method
        return 0 # default implementation
    
class Circle(Shape):   # child inherits from Shape
    def __init__(self, radius):
        super().__init__("Circle")  # call parent constructor
        self.radius = radius    # specific attribute

    def area(self): # override parent method   
        return 3.14 * self.radius * self.radius
    
class Square(Shape):   # child inherits from Shape
    def __init__(self, side):
        super().__init__("Square")
        self.side = side    # specific attribute

    def area(self): # override parent method   
        return self.side * self.side
    
# both Circle and Square inherit 'name' attribute and 'area' method from Shape

circle = Circle(5)
square = Square(4)

print(circle.name)        # "Circle" (inherited from Shape)
print(square.name)      # "Square" (inherited from Shape)

# polymorphism
def print_area(shape):   # takes any shape
    print(f"{shape.name} area: {shape.area()}")  # calls appropriate area()

# same method call, different behaviors
print_area(circle)   # Circle area: 78.5"
print_area(square)   # Square area: 16"

# or with a list
shapes = [Circle(3), Square(5), Circle(2)]  # Create a list of shapes
for shape in shapes:
    print_area(shape)  # calls the correct area() method based on object type

# # # ----------------------------------------------------------------- # # #

