def students(*s):  # * before variable means take all argument mentioned inside function
    for i in s:
        print(f"studen name {i}")


students("mayur", "adesh", "vaibhav")


# def student2(*s, a): # in this case age(a) wont find because the argument placed inside
# the function name will all take s
#     for i in s:
#         print(f"student name {i} age {a}")
#
#
# student2("mayur", "adesh", "vaibhav", 24)

def student3(a, *s):  # so in this case, the whole key will be divided into
    # two parts, here a variable will take only the first argument
    # & the remaining argument will be assigned to s variable
    for i in s:
        print(f"student name :{i}, age: {a}")


student3(19, "mayur", "vaibhav", "adesh")  # mayur 19, vaibhav 19, adesh 19


# NOTE: if we only print s variable, it will return value in tuple


# with argument 3 passing to function
def student4(s1, s2, s3):
    print(s1, s2, s3)


# student4("mayur","adesh","vaibhav") # by default, the argument will take the value in the sequence
# we can explicitly assign the value to the arguments
student4(s1="mayur", s3="vaibhav", s2="adesh")


# Arbitrary keyword items
# use this case to get value in the form of dictionary, so u must give some key to value
def student5(**s):
    print(s)


student5(s1="mayur", s2="adesh", s3="vaibhav")


# default argument/parameter
# if you want to give some default value to an argument, just -
# do like this functionName(argumentName = value) that's it
def weight(a=60):
    print(f"my weight is {a}")


weight(70)
