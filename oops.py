#encapsulation 
class Bank:
    def __init__(self):
        self.__balance = 1000   

    def deposit(self, amt):
        self.__balance += amt

    def show(self):
        print(self.__balance)

b = Bank()
b.deposit(500)
b.show()
#inheritance
class Animal:
    def speak(self):
        print("Speaking")

class Dog(Animal):
    def bark(self):
        print("Barking")

d = Dog()
d.speak()
d.bark()
#polymorphism
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()     

d.sound()
c.sound()
#abstraction
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass

class B(A):
    def show(self):
        print("Hello")

b = B()
b.show()
