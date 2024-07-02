def count(s, value):
    """统计在序列s中出现了多少次值为value的元素"""
    total, index = 0, 0
    while index < len(s):
        if value == s[index]:
            total = total + 1
        index = index + 1
    return total

digits = [0, 1, 2, 3, 4, 5, 6, 0]
print(count(digits, 0))
    