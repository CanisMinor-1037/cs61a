def fib(n):
    pred, curr = 0, 1
    k = 2
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

result = fib(8)
assert fib(2) == 1, "第2个斐波那契数应该是1"
assert fib(3) == 1, "第3个斐波那契数应该是1"
assert fib(50) == 7778742049, "在第50个斐波那契数发生Error"