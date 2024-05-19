def student(s):
    for i in s:
        print(i)


s = ["mayur", "adesh", "vaibhav"]
student(s)


# special or foolish case, even if you mention the required type to argument, it will work nonsense python
def student2(s: list):
    for i in s:
        print(i)


student2("himanshu")


#
def student3(s: list) -> list:  # want a specific input type to argument use
    # functionName(argumentName:type), want a specific return type in function
    # use functionName(argumentName:type) -> type, this last arrow type is for specific return type
    Teachers = ["t1", "t2", "t3"]
    combine = Teachers + s
    return combine


s = ["mayur", "vaibhav", "adesh"]
print(student3(s))


# find average of a numeric list
def average(scores: list) -> float:
    sum = 0
    for i in scores:
        sum += i
    avg = sum / len(scores)
    return avg


num = [1, 2, 3, 4, 5]
print(average(num))
