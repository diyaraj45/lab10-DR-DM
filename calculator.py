# https://github.com/diyaraj45/lab10-DR-DM.git
#Partner 1 - Diya Raj
#Partner 2 - David Mendoza
import math

# First example
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if b == 0:
        raise ValueError
    else:
        return math.log(a, b)

def exp(a, b):
    return a ** b




