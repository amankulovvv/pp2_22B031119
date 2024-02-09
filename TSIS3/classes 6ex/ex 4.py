class Point():
    def __init__(some, a, b):
        some.a = a
        some.b = b 
    def show(some):
        print(f"point, ({some.a} {some.b})")
    def move(some, deltaA, deltaB):
        some.a += deltaA
        some.b += deltaB
    def dist(some, sec_point):
        return ((some.a - sec_point.x)**2 + (some.b - sec_point.y)**2)**0.5