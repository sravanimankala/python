#documentation on oops

#1.Classes and Objects
#Class: A class is a blueprint or template for creating objects. It defines the properties and behaviors that the objects created from it will have. A class encapsulates data for the object and methods to manipulate that data.
#Object: An object is an instance of a class. Once a class is defined, you can create many objects from it, each with its own state.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car make: {self.make}, Model: {self.model}")

# Creating objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.display_info()
car2.display_info()

#2.Encapsulation
#Encapsulation: refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit known as a class. It also involves controlling access to the data by using access modifiers such as private, protected, and public.
#In many OOP languages, encapsulation ensures that an object's internal state can only be modified through its defined methods, promoting modularity and reducing complexity.

class Person:
    def __init__(self, name, age):
        self.__name = name  # private variable
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

#3.Inheritance
#Inheritance is a mechanism where a new class (child or subclass) derives properties and behavior (methods) from an existing class (parent or superclass). This allows for code reuse and the creation of a hierarchical relationship between classes.

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks

#4.Polymorphism
#Polymorphism means "many shapes." It allows methods to be used interchangeably, even if they are of different types. It enables an object to take on multiple forms. The most common form of polymorphism is method overriding, where a subclass provides a specific implementation for a method defined in the parent class.
   
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

#5.Abstraction
#Abstraction is the process of hiding the complex implementation details of a system and exposing only the necessary parts. It allows a programmer to focus on high-level mechanisms and interactions without needing to understand the low-level details.
#In OOP, abstraction is typically achieved using abstract classes or interfaces.

from abc import ABC, abstractmethod

class Shape(ABC):
    abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2








