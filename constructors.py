# constructor is a way of initializing or giving values to the variable inside the class using class object

class student:
    id = 1
    name = "mayur"


student = student()  # creating an object of class
print(student.id)
print(student.name)


class student2:
    def __init__(self, ID: int, Name: str, Courses):
        self.ID = ID
        self.Name = Name
        # self.Courses = ["Math", "Physics", "Chemistry"] # this is hardcoded default value to the argument
        self.Courses = Courses


student = student2(1, "Mayur", ["Maths", "Physics", "Chemistry"])

print(student.Name)
