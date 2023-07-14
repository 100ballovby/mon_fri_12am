username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

if (username == 'admin' or username == 'superuser') and (password == 'admin123' or password == 'password123'):
    print('Доступ разрешен!')
else:
    print('Доступ запрещен!')
