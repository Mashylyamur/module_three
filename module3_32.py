s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
То ли весь мир сошел с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

s_list = s.split()
for i in s_list:
    if len(i) < 5:
        print(i)

