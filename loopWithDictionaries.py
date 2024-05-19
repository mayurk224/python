dictionary = {
    # Key : Values
    "Brand": "Bmw",
    "Model": "M4",
    "Year": 2014,
    "Km Driven": 2044,
    "Price": 200000
}

for i in dictionary.items():
    print(i)  # this will print items as tuples. ex (key, value)

for i, x in dictionary.items():
    print(i, x)  # this way will separate both key and value by space

# want to print only value without use any method
for i in dictionary:
    print(dictionary[i])

# want to print only key
for i in dictionary.keys():
    print(i)

# make a copy of the dictionary
dictionary2 = dictionary.copy()
print(dictionary2)
dictionary3 = dict(dictionary)  # this will also work the same as the previous lines
print(dictionary3)
