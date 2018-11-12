class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'Price: $' + str(self.price)
        print 'Max Speed: ' + self.max_speed
        print 'Miles: ' + str(self.miles)
    
    def ride(self):
        print 'Riding'
        self.miles += 10
        return self

    def reverse(self):
        print 'Reversing'
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(200, '25mph')
bike2 = Bike(300, '40mph')
bike3 = Bike(500, '50mph')

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()