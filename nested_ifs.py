# lecture 9 : Nested ifs Statement

# Equals : a == b
# Not Equals : a != b
# Less than : a < b
# Less than or Equal to : a <= b
# Greater than : a > b
# Greater than or Equal to : a >= b

# The above all^ 6 condition will all return boolean value
print("This is the sample ans : ", 5 == 5)  # ex. of Equals , which will return True as Boolean value

# NOTE : Indentation( 1 Tab ) & Reformation( 1 space before and after the operators ) is compulsory to write a clean code
# NOTE : in case if statement is true then , elif statement will not execute

# else keyword is used for a default condition for if statement means if and elif condition both get False then else block will be executed
# else keyword can be used after if block or elif block only


a = 23
b = 43

# This is the one Standard way of writing if elif else block
print("Standard if elif else ans :")
if a > b:
    print("if statement")
elif b >= a:
    print("1st elif")
elif a == b:
    print("2nd elif")
else:
    print("else statement")

print("Single line if elif else ans :")
# This is the another way of writing if elif else block
print("if statement") if a > b else print("1st else if") if a != b else print("2nd else if") if a == b else print(
    "else statement")


# Test Cases

c = 23
d = 54
e = 26

print("Answer using and operator :")
if c < d and e < d:  # here, and operator will check both condition in if statement
    print("if statement")
elif d == e:
    print("1st elif statement")
elif d < c:
    print("2nd elif")
else:
    print("else statement")


print("Answer using or operator :")
if e > d or c < d:  # here, or operator will check both condition in if statement,
    print("if statement")
elif d == e:
    print("1st elif statement")
elif d < c:
    print("2nd elif")
else:
    print("else statement")


print("Answer using multiple operator :")
if (e > d and c < d) or c == d:  # here, first and operator will get output then it will match with or operator
    print("if statement")
elif d == e:
    print("1st elif statement")
elif d < c:
    print("2nd elif")
else:
    print("else statement")


# Nested ifs

f = 43
g = 34
h = 83

print("Nested ifs test cases :")
if f > g:   # here, its true so it move to 2nd line
    if h > f:   # here, its also true, so it move to 3rd line
        print("if inside if printed")
    elif g < h:   # here, elif neglected becoz upper if statement is true
        print("if inside elif printed")
elif h < f:     # here, this elif is also neglected becoz upper if block is getting true value
    print("if block elif print")
else:   # here, else won't print becoz if is true
    print("else printed")
