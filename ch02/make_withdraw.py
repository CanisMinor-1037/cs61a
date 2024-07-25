def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if balance > amount:
            balance = balance - amount
            return balance
        else:
            return '余额不足'
    return withdraw

withdraw = make_withdraw(100)
print(withdraw(25))
print(withdraw(25))
