class SomeClass:
    #fields and methods of the class
    attr1 = 42
    attr2 = "Hello, World!"

    def method1(self, x):
        return 2*x

class Point:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)



obj = SomeClass()
print(obj.attr1)
print(obj.attr2)
print("------")
print(obj.method1(4))

p = Point(13, 14, 15)
print(p.coord)

input()
