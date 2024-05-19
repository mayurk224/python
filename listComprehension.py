# lecture 23 : List Comprehension

# List Comprehension: is a way to creating a list

fruits = ["apple", "banana", "cheery", "kiwi", "jackfruit", "orange"]
newlist = []

# way 1: simple way
for i in fruits:
    if 'a' in i:
        newlist.append(i)

print(newlist)

# way 2: list comprehension
newlist2 = [i for i in fruits if
            'a' in i]  # here first `i` is a variable, then `for i in fruits` is a for loop , `if 'a' in i` here if conditional statement & here `i` is a first variable . and in default it automatically append items/objects in newlist
print(newlist2)



list = [i for i in range(11) if i < 5]
print(list)
