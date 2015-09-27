__author__ = 'Admin'
def interest(money: int, rate, month: int):
    money1 = money
    for i in range(month):
        money1 += money1 * rate
    return money1, money1 - money

print(interest(1000,0.1,4))