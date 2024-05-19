# lecture 12: The for loop


# for loop : We use `for` loops in Python to iterate over a sequence (like a list, tuple, or string) or an iterable object.
#            It allows us to execute a block of code repeatedly for each item in the sequence, simplifying tasks like iterating
#            through collections, processing data, and performing repetitive operations efficiently.


# ex.1 of for loop using list, a list didn't teach yet

# fruits = ["Banana", "Apple", "Grapes", "Pineapple"]
fruits = [1, 2, 3, 4, 5, 5, 6]
for Variable in fruits:
    print(Variable)  # if we print variable then simply it returns 1-6 no.
    # print(fruits)   # if we print an fruit array, then it will print a whole array at max index in that array
    # means if there are 6 indexs then the whole array will print 6 time

# ex.2: for loop with string

Var = "Mayur Kamble"
for i in Var:
    print(i)
    # here each letter consider as index, space is also consider as letter

# ex.3: for loop using break and continue keyword

Var2 = "Mayur Kamble"
for j in Var2:
    if j == " ":
        break  # basically break keyword stop the loop if the condition becomes true
    print(j)

Var3 = "Mayur Kamble"
for k in Var3:
    if k == "M":
        continue  # continue keyword will skip the condition value and move forward & complete the loop
    print(k)


# ex.4: for loop using an array with string

Var4 = ["Banana", "Apple", "grapes", "Mango"]
for l in Var4:
    if l == "grapes":
        # break
        continue
    print(l)
