# passing value for function from outside,
# just insert the variable name inside the function circular brackets

def volOfCylinder(h, r):
    a = 3.14 * (r * 2)
    vol = a * h
    print(round(vol))


# volOfCylinder(5, 2.5)
# if we don't give required parameters for the function, it will
# return an error of MISSING NO. OF ARGUMENTS


# get user input from console as height and radius for volOfCylinder()
h = float(input("enter height of cylinder \n"))
r = float(input("enter radius of cylinder \n"))
volOfCylinder(h, r)
