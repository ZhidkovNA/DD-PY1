salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

while months >= 1:
    if months > 1:
        spend = spend + spend * 0.03
        #print(spend)
        need_money = need_money + spend - salary
        months = months - 1
        #print(months)

    else:
        need_money = need_money + 6000 - salary
        months = months - 1
        #print(months)


#print(need_money)

# TODO Оформить решение
#print(months)
print(round(need_money))
