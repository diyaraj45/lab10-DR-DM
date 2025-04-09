import math

# calculator.py
# - Defines functions used to create a simple calculator

# First example
def add(a, b):
    a + b

def sub(a, b):
    a - b

def mul(a, b):
    a * b

def div(a, b):
    b/a
    raise ZeroDivisionError if a == 0 else b/a

def log(a, b):
    log(a, b)
    raise ValueError if b == 0 else log(a, b)

def exp(a, b):
    a ** b
    return a + b

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




