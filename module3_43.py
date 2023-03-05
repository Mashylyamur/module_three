import json
data = {}
with open('registr.json', 'w') as f:
    json.dump(data, f)
def register(login, passwd):
    with open('registr.json', 'r') as f:
        data = json.load(f)
    if login not in data.keys():
        data[login] = passwd
        with open('registr.json', 'w') as f:
            json.dump(data, f)
            print('Регистрация успешна!')
    else:
        print('Пользователь уже существует')
def login_function(login, passwd):
    with open('registr.json', 'r') as f:
        data = json.load(f)
    if login in data.values():
        data[login] = passwd
        print('Вход успешный')
    else:
        print('Пароль неверный')

while True:
    q1 = input('Вход или регистрация?')
    if q1 == 'регистрация':
        register(input('Логин: '), int(input('Пароль: ')))
    elif q1 == 'вход':
        login_function(input('Логин: '), int(input('Пароль: ')))
    else:
        break
