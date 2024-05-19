# lecture 7 : elif Statement

# Equals : a == b
# Not Equals : a != b
# Less than : a < b
# Less than or Equal to : a <= b
# Greater than : a > b
# Greater than or Equal to : a >= b

# The above all^ 6 condition will all return boolean value
print(5 == 5)  # ex. of Equals , which will return True as Boolean value

# NOTE : Indentation( 1 Tab ) & Reformation( 1 space before and after the operators ) is compulsory to write a clean code

a = 12
b = 24

if b < a:                       # here, if the conditon is true then it will execute another line, if its false then it'll move on another statement ( elif block )
    print("if ans :",a)         # here, no Output
elif a < b:
    print("elif ans :",a)

# NOTE : in case if statement is true then , elif statement will not execute