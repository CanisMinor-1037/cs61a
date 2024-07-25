def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if balance > amount:
            # 更改了withdraw栈帧之外的变量balance
            balance = balance - amount
            return balance
        else:
            return '余额不足'
    return withdraw

# balance变量只能在withdraw共享，程序其他部分无法访问
withdraw = make_withdraw(100)
print(withdraw(25))
print(withdraw(25))

# withdraw2共享新的balance变量
withdraw2 = make_withdraw(200)
print(withdraw2(25))
print(withdraw2(25))