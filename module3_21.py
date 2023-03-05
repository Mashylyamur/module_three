l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
l_repeat = []
for i in l:
    if l.count(i) == 2:
        l_repeat.append(i)
print(l)
print(l_repeat)

