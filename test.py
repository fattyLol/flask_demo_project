class Vehicle:
    def __init__(self, name, price, velocity):
        self.name = name
        self.price = price
        self.velocity = velocity

    def ride(self):
        print(self.name, ' vrom vrom')


class Car(Vehicle):
    def __init__(self, name, price, velocity):
        Vehicle.__init__(self, name, price, velocity)


bmw = Car('BMW', 15000, 220)

bmw.ride()
