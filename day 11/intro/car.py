class car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def display(self):
        print("Car Brand:", self.brand)
        print("Car Speed:", self.speed)
c1 = car("Toyota", 120)
c1.display()
c2 = car("Honda", 150)
c2.display()