class Person:
    def __init__(self, gender, age, height):
        self.gender = gender
        self.age = age
        self.height = height

    def printName(self):
        print(f'Gender :{self.gender}, age :{self.age}, height : {self.height}')


# what if we add extra parameter
# if you made some changes in the class don't use pass keyword
class Student(Person):
    def __init__(self, gender, age, height, year):
        self.year = year
        super().__init__(gender, age, height)

    def printName2(self):
        print(f'Gender :{self.gender}, age :{self.age}, height : {self.height}, year : {self.year}')


stud = Student("male", 19, 188, 2022)
stud.printName2()


# std = Student("Female", 25, 168)
# std.printName()


class vehicles:
    def __init__(self, brand, topSpeed, hp):
        self.brand = brand
        self.topSpeed = topSpeed
        self.hp = hp

    def Speed(self):
        if self.topSpeed < 100:
            print("Slow")
        elif 100 < self.topSpeed < 100:
            print("Normal")
        else:
            print("Fast")


class car(vehicles):
    def __init__(self, brand, topSpeed, hp, distance):
        self.distance = distance
        super().__init__(brand, topSpeed, hp)

    def Speed(self):
        if self.topSpeed < 80:
            print("Slow")
        elif 100 < self.topSpeed < 80:
            print("Normal")
        else:
            print("Fast")


class bike(vehicles):
    def __init__(self, brand, topSpeed, hp, fuel):
        self.fuel = fuel
        super().__init__(brand, topSpeed, hp)

    def Speed(self):
        if self.topSpeed < 80:
            print("Slow")
        elif 100 < self.topSpeed < 80:
            print("Normal")
        else:
            print("Fast")


# Creating instances of Car and Bike
my_car = car("Toyota", 110, 150, 500)
my_bike = bike("Yamaha", 90, 100, 15)

# Accessing attributes and methods
print(f"My car's brand: {my_car.brand}")
print(f"My bike's brand: {my_bike.brand}")

my_car.Speed()  # Output: Normal
my_bike.Speed() # Output: Normal