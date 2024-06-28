from operator import getitem

pair = [10, 20]
print(pair)

x, y = pair
print(x)
print(y)

print(pair[0])
print(pair[1])

print(getitem(pair, 0))
print(getitem(pair, 1))