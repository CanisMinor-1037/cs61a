# rational(n, d)
# numer(x)
# denom(x)
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