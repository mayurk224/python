class Person:
    def __init__(self, gender, age, height):
        self.gender = gender
        self.age = age
        self.height = height

    def printName(self):
        print(f'Gender :{self.gender}, age :{self.age}, height : {self.height}')


class Student(Person):
    pass  # pass keyword is for is just for inherite above class as it is


std = Student("Female", 25, 168)
std.printName()


# Inheritance in Python is a feature of object-oriented programming that
# allows a class (called the child or subclass) to inherit attributes and
# methods from another class (called the parent or superclass).
# This promotes code reuse and establishes a hierarchical relationship
# between classes.


# Key points:
# - **Parent Class (Superclass)**: The class whose properties and methods are inherited.
# - **Child Class (Subclass)**: The class that inherits from the parent class.
# - **Single Inheritance**: A subclass inherits from one parent class.
# - **Multiple Inheritance**: A subclass inherits from multiple parent classes.

# Example: python
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


# Dog inherits speak() from Animal
my_dog = Dog()
my_dog.speak()  # Output: Animal speaks
my_dog.bark()  # Output: Dog barks

# Inheritance allows subclasses to inherit and extend the functionality of parent classes, facilitating code reuse and better organization.
