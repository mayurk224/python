# lecture 11 : Break and Continue Statements in While loops


# while loop example : Printing sum from 1 to 10
i = 1
sum = 0

while i < 11:
    sum += i
    i += 1
    # print(sum) # if you print this line using 1 tab and after while block line it'll get included in while loop
print(sum)  # if you want to print something after while loop then erase space before it

# while loop using else : printing average
j = 1
sum1 = 0

while j < 5:

    # TEST CASE 1 : if you declare variable inside the loop
    # sum1 = 0    # In this scenario, no matter how many times the loop iterates, sum1 will always start from 0 at the beginning of each iteration.
    # So, when the loop finishes and calculates the average outside the loop, sum1 will only hold the value of the last grade entered, divided by 5.
    # This behavior is not likely what you intend; you generally want to accumulate the grades across iterations to calculate the average correctly.
    # Therefore, it's better to declare the sum1 variable outside the loop, as you did in your original code.

    grade = int(input("Enter student Grade :\n"))
    sum1 += grade
    j += 1
else:
    print("Average is : ", sum1 / 4)
# QUESTION : Why we use j and sum1 variable outside the loop, whereas grade variable is declared inside the loop ?
# ANSWER : Every time the loop runs, it creates a new instance of variable


# while loop using break keyword
print("Below ans is using while loop with break keyword")
k = 1
while k < 5:
    print(k)
    if k == 3:
        break
    k += 1
print("Loop completed")
# QUESTION : Why its necessary to use break keyword to stop loop ?
# ANSWER : It allows you to terminate the loop's execution based on a certain condition, even if the loop's control expression


# ex.2 : while loop using break keyword
print("Below ans is using while loop with break keyword on user input, -1 to break")
l = 0
sum2 = 0
while l < 1000:
    grade1 = int(input("Enter Grade : \n"))
    sum2 += grade1
    l += 1
    if grade1 == -1:
        break

print(sum2 / l)
print("Loop Completed")

# ex.3 : same ex. like before with some change ,while loop using break keyword
print("Below ans is using while loop with break keyword on user input till loop is True , -1 to break")
m = 0
sum3 = 0
while True:  # as long the loop is getting value true, the loop will continue
    grade2 = int(input("enter grade :"))
    sum3 += grade2
    m += 1
    if grade2 == -1:
        break

print(sum3 / m)
print("Loop Completed")


# while loop using continue keyword

# QUESTION : why we use continue keyword ?
# ANSWER : The `continue` keyword in Python is used to skip the rest of the code inside a loop for the current
#          iteration and proceed to the next iteration. It allows you to skip certain iterations of a loop based on a
#          condition without exiting the loop entirely.

print("Printing no from 1-10 & removed no 3")
n = 0
while n < 10:
    n += 1
    if n == 3:
        continue
    print(n)
print("Loop Completed")
