# functions are combining few lines of code inside a big block of code

height = 5
radius = 3.5
area = 3.14 * (radius ** 2)
volume = area * height
print(volume)  # this will give a long float value
print(round(volume, 5))  # this round() method will give a float value up to 5 no.


# functions are created by using def keyword and function name after it
# ex: calculate the vol of cylinder
def volofcylinder():
    h = 5
    r = 3.5
    a = 3.14 * (r ** 2)
    v = a * h
    print(round(v))


volofcylinder()


# create a function that loops through the list of student
# names and print each name sequentially

def studentNames():
    List = ["Mayur", "Adesh", "Vaibhav"]
    for i in List:
        print(i)


studentNames()
