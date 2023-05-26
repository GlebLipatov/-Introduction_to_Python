main_menu = ['Основное меню: \n',
             '\n1 - Показать все контакты.',
             '\n2 - Найти контакт.',
             '\n3 - Добавить контакт.',
             '\n4 - Изменить контакт',
             '\n5 - Удалить контакт',
             '\n6 - Сохранить изменения',
             '\n0 - Выход.',
             '\n\nВыберете пункт меню: ']

def print_menu(menu):
    for item in menu:
        print(item, end='')

def print_contacts(contacts: dict):
    FIRST_NAME = 0
    LAST_NAME = 1
    for contact in contacts:
        tel = contact
        first_name = contacts[contact][FIRST_NAME].capitalize()
        last_name = contacts[contact][LAST_NAME].capitalize()
        print(f'\nПолное имя: {first_name} {last_name}'
              f'\nИмя: {first_name}'
              f'\nФамилия: {last_name}'
              f'\nТелефон: {tel}'
              f'\n')
def find():
    print(f'\nВведите данные контакта: ', end='')
def not_found():
    print(f'\nТакого контакта нет.\n')


def input_first_name():
    print(f'\nВведите имя: ')


def input_last_name():
    print(f'\nВведите Фамилию: ')


def input_tel_number():
    print(f'\nВведите номер телефона: ')


def print_contacts_change(contacts):
    FIRST_NAME = 0
    LAST_NAME = 1
    TEL = 2
    for contact in contacts:
        id = contact
        first_name = contacts[contact][FIRST_NAME].capitalize()
        last_name = contacts[contact][LAST_NAME].capitalize()
        tel = contacts[contact][TEL]
        print(f'\n{id} - {first_name} {last_name}: {tel}')
    print('\nВыберите контакт: ', end='')


def what_change():
    print(f'\nЧто изменить: '
          f'\n1 - Имя.'
          f'\n2 - Фамилию.'
          f'\n3 - Телефон.'
          f'\n\nВыберете пункт меню: ')


def goodbye():
    print('Пока')

def alert():
    print('Необходимо ввести цифры от 0 до')