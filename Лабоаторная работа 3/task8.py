money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

money_capital += salary - spend
spend += spend * 0.05
month += + 1

while money_capital > 0:
    money_capital += salary - spend
    spend += spend * 0.05
    month += + 1

print(money_capital)
month -= 1

print(month)
