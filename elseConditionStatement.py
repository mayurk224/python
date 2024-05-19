# lecture 8 : else Statement

# Equals : a == b
# Not Equals : a != b
# Less than : a < b
# Less than or Equal to : a <= b
# Greater than : a > b
# Greater than or Equal to : a >= b

# The above all^ 6 condition will all return boolean value
print(5 == 5)  # ex. of Equals , which will return True as Boolean value

# NOTE : Indentation( 1 Tab ) & Reformation( 1 space before and after the operators ) is compulsory to write a clean code
# NOTE : in case if statement is true then , elif statement will not execute

# else keyword is used for a default condition for if statement means if and elif condition both get False then else block will be executed
# else keyword can be used after if block or elif block only

a = 12
b = 14

if a > b:                                           # here, if is False. so it'll analyze elif
    print("if statement executed")
elif b < a:                                         # here, elif is also False, so it'll analyze another elif
    print("first elif statement executed")
elif a >= b:                                        # here, again elif is getting False, so it'll analyze of next elif . if there is no elif then it'll execute else statement
    print("second elif statement executed")
else:                                               # here, else statement will print becoz of all above if & elif got False value.
    print("else statement executed")
