# lecture 6 : The if Statement

# if statement is also called as control flow
# if statement means. if certain condition match then do certain thing, if not then do another certain thing


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
if b < a:           # here, if the condition matches ( condition is True ) then and then it will proceed the block , if the condition not matches ( condition is false ) then it will not proceed and give no value in output
    print(a)        # here, no output in output box

c = "Mayur"
d = "Mayur"
if c == d:          # here, == operator will match each letter in terms of comparing string to string
    print(d)
