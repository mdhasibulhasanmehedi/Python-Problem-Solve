

class rectangle:
    area = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length*self.width)


length = int(input('input length:'))
width = int(input('input width:'))
obj = rectangle(length, width)
print(obj.area())