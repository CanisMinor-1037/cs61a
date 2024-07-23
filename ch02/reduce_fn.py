from operator import mul

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

print(reduce(mul, [2, 4, 8], 1))