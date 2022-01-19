import math


class circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return (self.r*2*math.pi)


cin = int(input())
obj = circle(cin)
print('print radius:', obj.r)
print('print circle area:', obj.area())
