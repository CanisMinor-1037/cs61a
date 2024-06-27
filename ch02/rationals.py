from math import gcd
# rational(n, d)
# numer(x)
# denom(x)
def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rationals(x, y):
    nx, ny = numer(x), numer(y)
    dx, dy = denom(x), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    nx, ny = numer(x), numer(y)
    dx, dy = denom(x), denom(y)
    return rational(nx * ny, dx * dy)
    
def print_rational(x):
    print(numer(x), '/', denom(x))
    

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def square_rational(x):
    return mul_rationals(x, x)

def square_rational_violating_once(x):
    return rational(numer(x) * numer(x), denom(x) * denom(x))

def square_rational_violating_twice(x):
    return [x[0] * x[0], x[1] * x[1]]

half = rational(1, 2)
third = rational(1, 3)

# print_rational(half)
# print_rational(mul_rationals(half, third))
# print_rational(add_rationals(half, third))
# print_rational(add_rationals(third, third))
