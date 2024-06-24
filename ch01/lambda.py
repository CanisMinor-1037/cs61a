s = lambda x: x * x
#print(s)
#print(s(12))

def compose1(f, g):
    return lambda x: f(g(x))

f = compose1(lambda x: x * x, lambda x: x + 1)
print(f(12))