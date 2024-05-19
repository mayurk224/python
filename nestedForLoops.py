# lecture 14: Nested for loop

list1 = ["Banana", "Apple", "Grapes"]
list2 = ["Yellow", "Black", "Green"]

for i in list1:
    for j in list2:
        print(i, j)

for k in range(5):
    pass  # pass keyword is like null, means this loop won't return anything

a = 5
b = 4
if a > b:
    pass
print("Nothing")
