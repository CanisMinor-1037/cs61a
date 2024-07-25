numerals = {'I': 1.0, 'V': 5, 'X': 10}
print(numerals['X'])

numerals['L'] = 50
numerals['I'] = 1
print(numerals['L'])
print(numerals['I'])

print(numerals.values())
print(numerals.keys())
print(numerals.items())

dict1 = dict([(3,9),(4,16),(5,25),(6,36)])
print(type(dict1))
print(dict1)

dict2 = {(1,2):3}
print(dict2)

# dict3 = {(1,[2]):3}
# print(dict3)

print(numerals.get('I', 0))
print(numerals.get('XI', 0))

print({x: x*x for x in range(3, 7)})