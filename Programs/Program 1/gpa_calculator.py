
# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Austin Hull, Peter Mitzel
# Last Modified: September 18, 2017 
# ---------------------------------------
# Calculates GPA based on user inputs.
# ---------------------------------------

import math

def translate(score):
    if score == "A" or score == "a":
        return 4.0
    elif score == "A-" or score == "a-":
        return 3.7
    elif score == "B+" or score == "b+":
        return 3.3
    elif score == "B" or score == "b":
        return 3.0
    elif score == "B-" or score == "b-":
        return 2.7
    elif score == "C+" or score == "c+":
        return 2.3
    elif score == "C" or score == "c":
        return 2.0
    elif score == "C-" or score == "c-":
        return 1.7
    elif score == "D+" or score == "d+":
        return 1.3
    elif score == "D" or score == "d":
        return 1.0
    elif score == "F" or score == "f":
        return 0.0

#a = credit, b = pointscale, c = overallpoints, d = overallhrs, e = classgpa

def math(a, b, c, d):
    e = (a * b)
    c = (c + e)
    d =(d + a)
    return c, d, e

overallhrs = 0
overallpoints = 0
count = 0

classes = int(input("Enter the number of courses you are taking: "))
print()

for count in range(count, classes):
    grade = input("Enter the grade for course {:d}: ".format(count + 1))
    credit = int(input("Enter the credits for course {:d}: ".format(count + 1)))
    print()

    pointscale = translate(grade)
   
    overallpoints, overallhrs, classgpa = math(credit, pointscale, overallpoints, overallhrs)

gpa = overallpoints / overallhrs
    
print("Your GPA is {0:.2f}".format(gpa))
