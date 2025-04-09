import math

# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if b == 0:
        raise ValueError
    else:
        return math.log(a, b)

def exponential(a, b):
    return a ** b







