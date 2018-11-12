class Underscore(object):
    def map(self, ls, func):
        output = []
        for item in ls:
            output.append(func(item))
        return output
    
    def reduce(self, ls, func, memo):
        output = memo
        for item in ls:
            output = func(output, item)
        return output
    
    def find(self, ls, func):
        for item in ls:
            if func(item):
                return item
        return None
    
    def filter(self, ls, func):
        output = []
        for item in ls:
            if func(item):
                output.append(item)
        return output
    
    def reject(self, ls, func):
        output = []
        for item in ls:
            if not func(item):
                output.append(item)
        return output


_ = Underscore()

print _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

print _.map([1,2,3,4,5,6], lambda x: x*5)

print _.find([1,2,3,4,5,6], lambda x: x%2 == 0)

print _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

print _.reduce([1,2,3], lambda memo, x: memo + x, 0)