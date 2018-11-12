class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
    def display(self):
        print "Call ID: {}\nCaller name: {}\nCaller phone number: {}\nTime of call: {}\nReason for call: {}".format(self.id, self.name, self.number, self.time, self.reason)


class CallCenter(object):
    def __init__(self, calls=[]):
        self.calls = calls
        self.queue_size = len(self.calls)
    
    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self):
        self.calls.pop(0)
        return self

    def remove_number(self, number):
        for i, call in enumerate(self.calls):
            if call.number == number:
                self.calls.pop(i)
                break
        return self

    def sort_calls(self):
        def numeric_compare(x, y):
            if x - y > 0:
                return 1
            elif x - y < 0:
                return -1
            else:
                return 0
        self.calls.sort(cmp=numeric_compare, key=lambda call: call.time)
        return self

    def info(self):
        for call in self.calls:
            print "Name: {}\nPhone number: {}".format(call.name, call.number)
        print "Length of queue: {}".format(len(self.calls))


call1 = Call(1, 'Charlie', 5555555, 9.5, 'complaint')
call2 = Call(2, 'Emily', 7777777, 10, 'compliment')
call3 = Call(3, 'Bobby', 7777777, 9, 'compliment')

cc = CallCenter()
cc.add(call1).add(call2).add(call3)
cc.sort_calls().info()