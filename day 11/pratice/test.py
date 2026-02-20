class Test:
    x = 5

a = Test()
b = Test()

a.x = 10

print(Test.x)
print(a.x)
print(b.x)
