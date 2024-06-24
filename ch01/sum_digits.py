def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last
    
print(sum_digits(9))
print(sum_digits(18117))
print(sum_digits(9437184))
print(sum_digits(11408855402054064613470328848384))
