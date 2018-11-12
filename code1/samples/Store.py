class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'
    
    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        return self.price * (1 + tax)

    def return_product(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'in box like new':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price *= 0.8
        return self

    def display_info(self)
        print 'Price: $' + str(self.price)
        print 'Name: ' + self.name
        print 'Weight: ' + str(self.weight)
        print 'Brand: ' + self.brand
        print 'Cost: $' + str(self.cost)
        print 'Status: ' + self.status
        return self

class Store(object):
    def __init__(self, products, address, owner):
        self.products = products
        self.address = address
        self.owner = owner
    
    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        self.products.remove(product)
        return self

    def inventory(self):
        for product in self.products:
            display_info(product)
        return self