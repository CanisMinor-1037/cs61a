def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

print([n for n in range(1, 1000) if sum(divisors(n)) == n])

# print(divisors(4))
# print(divisors(100))

