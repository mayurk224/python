# lecture 17: Modifying String

var = "Hello World"
print(var.upper())  # this upper() function is use to capitalize all letters in string

var2 = "Hello WORLD"
print(var2.lower())  # this lower() function is use to lower case all letters

var3 = "             HELLO WORLD"
print(var3.strip())  # this strip() function is use to remove starting extra spaces

var4 = "hello world"
print(var4.replace("h", "k"))

var5 = "hello world"
var5 = var4.replace("h", "k").replace("o", "x") # this is the simple way to replace individual multiple letter using replace() function
print(var5)

var6 = "hello world"
print(var6.split(" "))  # this split() function is use to separate the string in array format where letter or symbol is present inside split(" ") like here output is ['hello','world'] because it separated by space inside spilt
