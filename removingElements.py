# lecture 22: Removing Elements

var = ["apple", "banana", "cat", "dog", "elephant", "fox", "grapes"]
var.append("DragonFruit")  # this append function is used to insert only one object at a time at last index in an array

print(var)

var2 = ["hello", "How", "are", "you"]
print(var2)
var.extend(
    var2)  # this extend funtion is use to add two array, but the second array element will place after the first array elements
print(var)

var3 = ["we", "welcome", "you", "here"]
var3.remove("we")  # this remove function is use to remove an object, but only remove by the string, int value is not allowed
print(var3)

# to remove item by its index use pop() function
var4 = ["Hello", "my", "is", "mayur", "nice", "to", "meet", "you"]
var4.pop(4)  # if we use index greater than array size, it shows out of range exception
print(var4)

del var4[1] # this del keyword is use to delete object by its index by variable as parameter and variable parameter needs index as parameter
print(var4)

var4.clear()    # this clear function is use for to clear all objects/items in an array and return empty array
print(var4)
