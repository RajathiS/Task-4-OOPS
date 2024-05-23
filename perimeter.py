class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.141 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.141 * self.radius
Obj = Circle(9)
print("Area:", Obj.area())
print("Perimeter:", Obj.perimeter())
