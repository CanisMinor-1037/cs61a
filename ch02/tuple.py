tuple1 = 1, 2 + 3
print(type(tuple1))

tuple2 = ("the", 1, ("and", "only"))
print(tuple2)

print(type((10, 20)))

empty_tuple = ()
single_element_tuple = (10,)
print(type(empty_tuple))
print(type(single_element_tuple))

code = ('up', 'up', 'down', 'down') + ('left', 'right') * 2
print(code)
print(len(code))
print(code.count('up'))
print(code.index('right'))

list1 = [0, 1, 2]
has_mutable_element_tuple = (list1, 'up')
print(has_mutable_element_tuple)
has_mutable_element_tuple[0].reverse()
print(has_mutable_element_tuple)

a, b = 1, 2
print(a, b)