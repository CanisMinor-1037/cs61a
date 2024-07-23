from operator import add

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(x, reduced)
    return reduced

def keep_if(fn, s):
    return [x for x in s if fn(x)]

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

print(keep_if(perfect, range(1, 1000)))
