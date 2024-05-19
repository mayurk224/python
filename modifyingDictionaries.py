dictionary = {
    # Key : Values
    "Brand": "Bmw",
    "Model": "M4",
    "Year": 2014,
    "Km Driven": 2044,
    "Price": 200000
}

print(dictionary)
# only print key
print(dictionary.keys())
# only value
print(dictionary.values())

# modifying the Dictionary values by key
dictionary["Year"] = 2020
print(dictionary["Year"])
print(dictionary)

# adding new key value to dictionary
dictionary["Fuel Type"] = "Petrol"
print(dictionary)

# print only items from dictionary
print(dictionary.items())

# conditional statement with dictionary
if "Brand" in dictionary:  # conditional statement will only look for key in
    # dictionary, so if you put value then it wont work
    print("Yes")
else:
    print("No")

# another way to modify dictionary
dictionary.update({"Year": 2000})
print(dictionary)

# remove items from dictionary
dictionary.pop("Year")  # pop method is used to remove the whole key value as an item in
print(dictionary)

# want to remove list item & don't know key then use popItem() method
dictionary.popitem()
print(dictionary)

# NOTE : if you use pop() & popItem() one after another ,
# then only pop() method will work popItem() will not work

# another way to remove item
del dictionary["Km Driven"]
print(dictionary)

# remove the whole items from the dictionary
dictionary.clear()
print(dictionary)
