from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print p.x
print p.y

Circle = namedtuple('Circle',['x', 'y', 'r'])
c = Circle(4, 5, 6)
print c.x
print c.y
print c.r