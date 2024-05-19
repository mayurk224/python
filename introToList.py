# lecture 20: Introduction to List

# list: collections of variables, to write list use []
# The len() function is handy for getting the size of a collection, which can be useful for various tasks,
# such as iterating over elements or performing conditional checks.

var = ["Banana", "Mango", "Apple", "Grapes"]
print(len(var))  # len() function is use to give the no. of elements/items present in an array

var2 = [1, 5, 64, 94, 64, 82, 60]
print(len(var2))  # len() function avoid the repeated elements, so it counts only 1 time in an array

var3 = [1, "Apple", True, 6.45]
print(len(var3))  # for len() function it doesnt matter the type of data present in an array, it only count the elements inside an array

var4 = [1, "Apple", True, 6.45]
print(type(var4))  # type() function is use to identify the type of variable you mention inside it

var5 = list(("Banana", "Apple", "Mango", "Grapes")) # another way to print an array in output
print(var5)
print(len(var5))
