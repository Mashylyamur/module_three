import json
data = {}
with open('registration.json', 'w') as f:
    json.dump(data, f)
def register(login, passwd):
    with open('registration.json', 'r') as f:
        data = json.load(f)
    if login not in data.keys():
        data[login] = passwd
        with open('registration.json', 'w') as f:
            json.dump(data, f)
            print('Регистрация успешна!')
    else:
        print('Пользователь уже существует')

while True:
    q1 = input('Для регистрации в системе введите "enter"')
    if q1 == 'enter':
        register(input('Логин: '), int(input('Пароль: ')))
