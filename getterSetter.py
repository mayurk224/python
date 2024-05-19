class student2:
    def __init__(self, ID: int, Name: str, Courses):
        self.ID = ID
        self.Name = Name
        # self.Courses = ["Math", "Physics", "Chemistry"] # this is hardcoded default value to the argument
        self.Courses = Courses

    def __str__(self):
        return f'(Id = {self.ID}, Name = {self.Name}, Course = {self.Courses})'

    def GetId(self):
        return self.ID

    def GetName(self):
        return self.Name

    def GetCourses(self):
        return self.Courses

    def SetName(self, Value):
        self.Name = Value

    def SetID(self, Value):
        self.ID = Value

    def SetCourses(self, Value):
        self.Courses = Value


student = student2(1, "Mayur", ["Maths", "Physics", "Chemistry"])
student.SetID(3)
print(student.GetName())
print(student.GetId())



# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} is barking!")
#
#
# # Creating an instance of the Dog class
# my_dog = Dog("Buddy", 3)
#
# # Accessing attributes and methods of the instance
# print(my_dog.name)  # Output: Buddy
# print(my_dog.age)  # Output: 3
# my_dog.bark()  # Output: Buddy is barking!
