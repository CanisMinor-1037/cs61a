# f(x, y) -> g(x)(y)
def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

# g(x)(y) -> f(x, y)
def uncurry(g):
    def f(x, y):
        return g(x)(y)
    return f

pow_curried = curry(pow)
print(pow_curried(2)(3))

print(uncurry(pow_curried)(2, 3))