# Base Case: A base case is a condition that stops the recursion
# without a phase case. The recursion will continue indefinitely,
# leading to stack overflow. It is the simplest form of the problem
# that can solve directly.

# Recursive Case: the recursive case is the shared the function call
# itself with a Modified or reduced versions of the problem. Each recursive
# call should move closer in the base case.

# Function argument: in case regulatory call you typically pass argument that
# represent a smaller or simpler part of the problem.

# Return value: the function may need to combine or process the result from
# the recursive call to solve the original problem.

def factorail(n):
    # Base case
    if n == 0:
        return 1
    # Recursive Case
    else:
        # Function Argument
        return n * factorail(n - 1) # if all above if&else statement will
        # be comment out, the return statement will run infinitely until it out of memory


print(factorail(5))


# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two preceding ones, usually starting with 0 and 1. The sequence
# starts like this:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(n):
    # Base Case
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(8))  # here you can consider 8 as a position in series, like on position 8 the value is 21
