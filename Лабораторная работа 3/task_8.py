money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital >= 0:
    money_capital = salary + money_capital - spend * ((1 + increase) ** month)
    month += 1
else:
    month -= 1
# TODO Оформить решение
print(month - 2)
# Видимо ошибка в задаче. На лекции преподаватель сказал что есть ошибка в задаче.