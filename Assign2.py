"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

x = input("enter in a number that can be a float value: ")
y = input("enter in another number that can be a float value: ")

t = input("type yes if one of the numbers is the hypotenuse of a right triangle: ")

c = max(x,y)
b = min(x,y)

c = float(c)
b = float(b)

if t == "yes" :
    a = ((c**2)-(b**2))**0.5
    r = round(a,1)
    print(f"the missing side is {r} long")
