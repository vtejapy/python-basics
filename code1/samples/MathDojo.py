class MathDojo(object):
    def __init__(self):
        self.result = 0
    
    def add(self, *args):
        for item in args:
            if type(item) == list or type(item) == tuple:
                for i in range(0, len(item)):
                    self.result += item[i]
            else:
                self.result += item
        return self

    def subtract(self, *args):
        for item in args:
            if type(item) == list or type(item) == tuple:
                for i in range(0, len(item)):
                    self.result -= item[i]
            else:
                self.result -= item
        return self


print MathDojo().add(2).add(2, 5).subtract(3, 2).result

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result