def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

#print(square_root_newton(64))

def power(x, n):
    """返回x^n"""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_newton(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return power(x, n - 1) * n 
    return find_zero(f, df)

print(nth_root_newton(2, 64))
print(nth_root_newton(3, 64))
print(nth_root_newton(6, 64))