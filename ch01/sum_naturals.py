from doctest import testmod
from doctest import run_docstring_examples
def sum_naturals(n):
    """返回前 n 个自然数的和。
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total
testmod()
run_docstring_examples(sum_naturals, globals(), True)