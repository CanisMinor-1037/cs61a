from functools import reduce
from operator import mul
print(reduce(mul, range(1, 10), 1))