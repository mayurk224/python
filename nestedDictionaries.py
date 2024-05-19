myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2003
    },
    "child2": {
        "name": "tobby",
        "year": 2004
    },
    "child3": {
        "name": "line",
        "year": 2005
    }
}
print(myFamily)
# select child1
print(myFamily["child1"])
# select item & also key inside it
print(myFamily["child2"]["name"])
# modify
myFamily["child3"]["name"] = 'lenis'
print(myFamily["child3"])

# another way to write a nested dictionary
child1 = {
    "name": "Emil",
    "year": 2003
}
child2 = {
    "name": "tobby",
    "year": 2004
}
child3 = {
    "name": "line",
    "year": 2005
}
myFamily2 = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myFamily2)
