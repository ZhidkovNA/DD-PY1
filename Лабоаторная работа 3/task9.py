salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
need_money += spend - salary
months -= 1

while months >= 1:
    spend += spend * increase
    need_money += spend - salary
    months -= 1

print(round(need_money))
