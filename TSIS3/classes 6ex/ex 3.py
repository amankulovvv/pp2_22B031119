class Shape():
    def __init__(some):
        some.area = 0
    def area(some):
        return some.area
class Rectangle(Shape):
    def __init__(some, length, width):
        super().__init__()
        some.length = length
        some.width = width
    def area(some):
        some.area = some.length * some.width
        return some.area