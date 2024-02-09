class Shape():
    def __init__(some):
        some.area = 0
    def area(some):
        return some.area
class Square(Shape):
    def __init__(some, length):
        super().__init__()
        some.string = length
    def area(some):
        some.area = some.length * some.length
        return some.area