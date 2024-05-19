# lecture 21: Inserting Items

var = ["apple", "banana", "cat", "dog", "elephant", "fox", "grapes"]
print(var[0:4])  # this is string slicing

var2 = ["apple", "banana", "cat", "dog", "elephant", "fox", "grapes"]
var2[
    2] = "cucumber"  # to replace item with another , first give array variable, then in array mention the index with which you want to replace with then with = mention another string or anything
# var2[3:6] = "giraffe" # if we dont mention curly braces then this string with give unexpected output ['apple', 'banana', 'cucumber', 'g', 'i', 'r', 'a', 'f', 'f', 'e', 'grapes']
var2[3:6] = ["giraffe"]
print(var2)

var3 = ["apple", "banana", "cat", "dog", "elephant", "fox", "grapes"]
var3.insert(2, "peach")  # this insert function will only insert one object at a time
print(var3)
