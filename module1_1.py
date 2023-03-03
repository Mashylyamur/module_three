x = int(input('Сумма вклада'))
y = int(input('Ожидаемая сумма вклада'))
p = int(input('Процент'))
i = 0
while x < y:
    x *= 1 + p/100
    x = int(100 * x) / 100
    i += 1
print(i)
