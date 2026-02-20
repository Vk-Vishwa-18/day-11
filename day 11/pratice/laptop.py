class laptop:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def display(self):
        print("Laptop Model:", self.model)
        print("Laptop Price:", self.price)
c1 = laptop("Dell", 50000)
c1.display()
c2 = laptop("HP", 60000)
c2.display()