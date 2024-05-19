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

    def Average(self, Grade: list) -> float:
        sum = 0
        for i in Grade:
            sum += i

        avg = sum / len(Grade)

        return round(avg, 2)


student = student2(1, "Mayur", ["Maths", "Physics", "Chemistry"])
avg = student.Average([34, 58, 90.3, 40.5, 20, 10])
# del student # this will delete whole object
del student.Name  # this will delete a name component
print(avg)
print(student.GetName())
