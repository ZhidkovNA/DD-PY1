money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital > 0:
    if month == 0:
        money_capital = money_capital + salary - spend
        spend = spend + spend * 0.05
        month = month + 1
    else:
        money_capital = money_capital + salary - spend
        spend = spend + spend * 0.05
        month = month + 1

print(money_capital)
month = month - 1

# TODO Оформить решение
print(month)
