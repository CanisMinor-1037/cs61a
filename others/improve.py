from math import sqrt
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1 / guess + 1

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def golden_close(guess):
    return approx_eq(guess + 1, guess * guess)

#print(improve(golden_update, golden_close))
phi = 1 / 2 + sqrt(5) / 2

def improve_test():
    approx_phi = improve(golden_update, golden_close)
    assert approx_eq(approx_phi, phi), 'phi differs from its approximation'
    
improve_test()