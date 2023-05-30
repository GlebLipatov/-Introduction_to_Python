import text
FIRST_NAME = 0
LAST_NAME = 1
TEL = 2
COMMENT = 3
def show_title(message: str, max_length: int):
    print(f'{message:^{max_length}}')
    print('-' * max_length)

def show_menu(menu: list, title: str) -> int:
    max_length = max(get_max_length(title), get_max_length(menu))
    show_title(title, max_length)
    print(''.join(menu))
    choice = show_choice_menu(text.input_choice, len(menu), text.error_input_main_menu)

    return choice

def show_menu_search(menu: list, title: str, search_contacts: dict) -> int:
    max_length = max(get_max_length(title), get_max_length(menu))
    show_title(title, max_length)
    print(''.join(menu))
    choice = show_choice_menu_search(text.input_choice, text.error_input_search, search_contacts)

    return choice

def get_max_length(item, index: int = -1) -> int:
    max = 0
    if type(item) == list and index == -1:
        for element in item:
            if len(element) > max:
                max = len(element)
    elif type(item) == dict and index == -1:
        for element in item.values():
            if len(''.join(element)) > max:
                max = len(''.join(element))
    elif type(item) == dict and index == -2:
        for element in item:
            if len(str(element)) > max:
                max = len(str(element))
    elif type(item) == dict and index >= 0:
        for value in item.values():
            if len(value[index]) > max:
                max = len(value[index])
    elif type(item) == str:
        max = len(item)


    return max

def show_choice_menu(enter_message: str, menu_size: int, error: str) -> int:
    while True:
        input_from_user = input(f'\n{enter_message}')
        if input_from_user.isdigit() and 0 < int(input_from_user) <= menu_size:
            return int(input_from_user)
        else:
            print(f'!!! {error}{menu_size} !!!')

def show_choice_menu_search(enter_message: str, error: str, search_contacts: dict) -> int:
    points = ''
    for id in search_contacts:
        points += f'{id} '
    while True:
        input_from_user = input(f'\n{enter_message}')
        if input_from_user.isdigit():
            input_from_user = int(input_from_user)
            for id in search_contacts:
                if id == input_from_user:
                    return input_from_user
        else:
            print(f'!!! {error}{points} !!!')

def show_contacts(contacts: dict) -> int:
    margin = 13

    col_size_first_name = max(get_max_length(contacts, FIRST_NAME), len(text.first_name)) + margin
    col_size_last_name = max(get_max_length(contacts, LAST_NAME), len(text.last_name)) + margin
    col_size_tel = max(get_max_length(contacts, TEL), len(text.phone_number)) + margin
    com_size_comment = max(get_max_length(contacts, COMMENT), len(text.comment)) + margin

    table_size = col_size_first_name + col_size_last_name + col_size_tel + com_size_comment

    print('-' * table_size)
    print(f'{text.first_name:^{col_size_first_name}}|'
          f'{text.last_name:^{col_size_last_name}}|'
          f'{text.phone_number:^{col_size_tel}}|'
          f'{text.comment:^{com_size_comment}}')
    print('-' * table_size)
    for contact in contacts.values():
        print(f' {contact[FIRST_NAME].capitalize():<{col_size_first_name - 1}}|'
              f' {contact[LAST_NAME].capitalize():<{col_size_last_name - 1}}|'
              f'{contact[TEL]:^{col_size_tel}}|'
              f' {contact[COMMENT].capitalize():<{com_size_comment - 1}}')
    print('-' * table_size)

    return show_menu(text.back_to_main_menu, text.title_menu)


def show_search_contact(title: str) -> str:
    show_title(title, max(len(title), len(text.enter_contact_data)))
    input_from_user = input('\n' + text.enter_contact_data)
    return input_from_user


def show_add_contact(title: str) -> list:
    new_contact_data = []
    show_title(title, max(len(title), get_max_length(text.enter_new_data)))
    for data in text.enter_new_data:
        new_contact_data.append(input(data))
    return new_contact_data


def show_successfully_message(isAdd: bool, title: str) -> int:
    show_title('\n' + title, len(text.contact_added)) if isAdd else show_title(text.error, len(text.error))

    return show_menu(text.back_to_main_menu, text.title_menu)


def show_contacts_to_change(find_contacts: dict) -> int:
    margin = 13
    col_size_id = max(get_max_length(find_contacts, -2), len(text.id)) + margin
    col_size_first_name = max(get_max_length(find_contacts, FIRST_NAME), len(text.first_name)) + margin
    col_size_last_name = max(get_max_length(find_contacts, LAST_NAME), len(text.last_name)) + margin
    col_size_tel = max(get_max_length(find_contacts, TEL), len(text.phone_number)) + margin
    com_size_comment = max(get_max_length(find_contacts, COMMENT), len(text.comment)) + margin

    table_size = col_size_first_name + col_size_last_name + col_size_tel + com_size_comment + col_size_id

    print('-' * table_size)
    print(f'{text.id:^{col_size_id}}|'
          f'{text.first_name:^{col_size_first_name}}|'
          f'{text.last_name:^{col_size_last_name}}|'
          f'{text.phone_number:^{col_size_tel}}|'
          f'{text.comment:^{com_size_comment}}')
    print('-' * table_size)
    for contact in find_contacts:
        print(f' {contact:^{col_size_id - 1}}|'
              f' {find_contacts[contact][FIRST_NAME].capitalize():<{col_size_first_name - 1}}|'
              f' {find_contacts[contact][LAST_NAME].capitalize():<{col_size_last_name - 1}}|'
              f'{find_contacts[contact][TEL]:^{col_size_tel}}|'
              f' {find_contacts[contact][COMMENT].capitalize():<{com_size_comment - 1}}')
    print('-' * table_size)

    return show_choice_menu_search(text.enter_contact, text.error_input_main_menu, find_contacts)