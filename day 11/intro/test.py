class Car:
    wheels = 4

c1 = Car()
c2 = Car()

Car.wheels = 8

print(c1.wheels)
print(c2.wheels)
