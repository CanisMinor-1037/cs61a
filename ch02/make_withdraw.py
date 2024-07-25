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

# 两个名称都引用同一个函数
withdraw3 = make_withdraw(100)
withdraw4 = withdraw3
print(withdraw3(25))
print(withdraw4(25))