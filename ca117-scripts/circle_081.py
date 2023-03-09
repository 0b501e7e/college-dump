#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def midpoint(self, other):
        x = (other.x + self.x) / 2
        y = (other.y + self.y) / 2
        return Point(x, y)


class Circle(object):

    def __init__(self, radius=0, centre=None):
        if centre is None:
            centre = Point()
        self.radius = radius
        self.centre = centre

    def __add__(self, other):
        c = self.centre.midpoint(other.centre)
        r = self.radius + other.radius
        return Circle(c, r)

    def __str__(self):
        lines = list()
        lines.append("Centre: {}".format(self.centre))
        lines.append("Radius: {}".format(self.radius))
        return "\n".join(lines)


def main():
    p1 = Point()
    p2 = Point(4, 6)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)
    c3 = c1 + c2
    print(c3)

    p3 = Point(10, 10)
    c4 = Circle(p3, 15)
    c5 = c2 + c4
    print(c5)


if __name__ == '__main__':
    main()
