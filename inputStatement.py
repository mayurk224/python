# lecture 5 : Input Statements

# for taking input from user/keyboard then use  input() function
input("Enter your name : ") # ex. of taking input from keyboard
name = input("Enter your name : ") # ex. of storing input value in variable, but there is no limit in datatype that keyboard enter
print(name) # the output will be the text you wrote in output box, but it will neglect the hardcoded text

# setting limit of datatype should be entered in output box
name1 = str(input("Enter your name :")) # ex. of taking only string input from keyboard, here str is used for string variables
print("Your name is :",name1)
age = int(input("Enter your age : ")) # ex. of taking only number input from keyboard, here int is used for Integer variables
# NOTE : if the you tried to enter string value at the integer restriction , then ValueError exception will occure