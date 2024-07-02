def count(s, value):
    total = 0
    for element in s:
        if element == value:
            total = total + 1
    print(element)
    return total

digits = [0, 1, 2, 3, 4, 5, 6, 0]
count(digits, 0)