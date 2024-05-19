# dictionaries: is something similar to list except items are stored is in
# key value pairs, each element in the dictionary will have two thing key value
# of it and the actual value/element.
# in a simple way, it's just like data in json format

dictionary = {
    # key and value will be int as well and vise versa also
    # key must be unique and cant be repeated as well
    # if we use the same key again it will show warning msg & the value of that key will be considered with new key
    # "KEY": "VALUE"
    "Brand": "BMW",
    "Model": "M3",
    "Year": 2015,
    "km Driven": 15000,
    "Price": 2000000,
    25: "BMW M3"
}
print(dictionary)
print(len(dictionary))  # this will print the no. of key value pairs inside the dictionary
print(dictionary["Brand"])  # to fetch data from dictionary, we use square bracket with a key in double invert coma
# print(dictionary["hello"] # when there is no such key present in dictionary then it will show keyError

# another way to create a dictionary
dictionary2 = dict(Brand="m3", Price=15000)
print(dictionary2)
