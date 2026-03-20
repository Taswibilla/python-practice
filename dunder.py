#__init__
class Student:
    def __init__(self, name):
        self.name = name
student1 = Student("Alice")
print(student1.name) 
#__str__
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Taswi")
print(s)
#__str__
class A:
    def __str__(self):
        return "Hello"

a = A()
print(a)
#__len__
class A:
    def __len__(self):
        return 5

a = A()
print(len(a))
#__getitem__
class A:
    def __getitem__(self, i):
        return i * 2

a = A()
print(a[3])
#__eq__
class A:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

a = A(5)
b = A(5)

print(a == b)
#__setitem__
class A:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

a = A()
a["x"] = 10
print(a.data)
#__contains__
class A:
    def __contains__(self, x):
        return x == 10

a = A()
print(10 in a)
#__call__
class A:
    def __call__(self):
        print("Called")

a = A()
a()
#_--iter--&__next__
class A:
    def __init__(self):
        self.i = 1   # start
    def __iter__(self):
        return self  # iterator return
    def __next__(self):
        if self.i <= 3:
            val = self.i
            self.i += 1
            return val
        else:
            raise StopIteration
a = A()

for x in a:
    print(x)