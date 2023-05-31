import text

ID = 0
FIRST_NAME = 1
LAST_NAME = 2
PHONE_NUMBER = 3
COMMENT = 4


def show_title(message: str, max_length: int):
    print(f'{message:^{max_length}}')
    print('-' * max_length)


def show_menu(menu: list, title: str) -> int:
    width = get_menu_width(title, menu)
    show_title(title, width)
    print(''.join(menu))
    choice = show_choice_menu(text.input_choice, len(menu), text.error_input_main_menu)

    return choice


def show_menu_search(menu: list, title: str, search_contacts: dict) -> int:
    width = get_menu_width(title, menu)
    show_title(title, width)
    print(''.join(menu))
    choice = show_choice_menu_search(text.input_choice, text.error_input_search, search_contacts)

    return choice


def show_menu_add(title: str) -> list:
    new_data = []
    show_title(title, max(len(title), len(text.enter_new_data)))
    for data in text.enter_new_data:
        new_data.append(input(data))
    return new_data


def show_search(title: str) -> str:
    show_title(title, max(len(title), len(text.enter_contact_data)))
    input_from_user = input('\n' + text.enter_contact_data)
    return input_from_user


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


def show_successfully_message(title: str) -> int:
    show_title('\n' + title, len(title))
    return show_menu(text.back_to_main_menu, text.title_menu)


def show_contacts(contacts: dict) -> int:
    margin = 8

    col_width_first_name = max(get_column_width(contacts, FIRST_NAME), len(text.first_name)) + margin
    col_width_last_name = max(get_column_width(contacts, LAST_NAME), len(text.last_name)) + margin
    col_width_tel = max(get_column_width(contacts, PHONE_NUMBER), len(text.phone_number)) + margin
    com_width_comment = max(get_column_width(contacts, COMMENT), len(text.comment)) + margin

    table_width = col_width_first_name + col_width_last_name + col_width_tel + com_width_comment

    print('-' * table_width)
    print(f'{text.first_name:^{col_width_first_name}}|'
          f'{text.last_name:^{col_width_last_name}}|'
          f'{text.phone_number:^{col_width_tel}}|'
          f'{text.comment:^{com_width_comment}}')
    print('-' * table_width)
    for contact in contacts.values():
        print(f' {contact.first_name.capitalize():<{col_width_first_name - 1}}|'
              f' {contact.last_name.capitalize():<{col_width_last_name - 1}}|'
              f'{contact.phone_number:^{col_width_tel}}|'
              f' {contact.comment.capitalize():<{com_width_comment - 1}}')
    print('-' * table_width)

    return show_menu(text.back_to_main_menu, text.title_menu)


def show_contacts_to_change(find_contacts: dict) -> int:
    margin = 8

    col_width_id = max(get_column_width(find_contacts, ID), len(text.id)) + margin
    col_width_first_name = max(get_column_width(find_contacts, FIRST_NAME), len(text.first_name)) + margin
    col_width_last_name = max(get_column_width(find_contacts, LAST_NAME), len(text.last_name)) + margin
    col_width_tel = max(get_column_width(find_contacts, PHONE_NUMBER), len(text.phone_number)) + margin
    com_width_comment = max(get_column_width(find_contacts, COMMENT), len(text.comment)) + margin

    table_width = col_width_first_name + col_width_last_name + col_width_tel + com_width_comment + col_width_id

    print('-' * table_width)
    print(f'{text.id:^{col_width_id}}|'
          f'{text.first_name:^{col_width_first_name}}|'
          f'{text.last_name:^{col_width_last_name}}|'
          f'{text.phone_number:^{col_width_tel}}|'
          f'{text.comment:^{com_width_comment}}')
    print('-' * table_width)
    for contact in find_contacts.values():
        print(f' {contact.get_contact_data()[ID]:^{col_width_id - 1}}|'
              f' {contact.get_contact_data()[FIRST_NAME].capitalize():<{col_width_first_name - 1}}|'
              f' {contact.get_contact_data()[LAST_NAME].capitalize():<{col_width_last_name - 1}}|'
              f'{contact.get_contact_data()[PHONE_NUMBER]:^{col_width_tel}}|'
              f' {contact.get_contact_data()[COMMENT].capitalize():<{com_width_comment - 1}}')
    print('-' * table_width)

    return show_choice_menu_search(text.enter_contact, text.error_input_main_menu, find_contacts)


def get_menu_width(title: str, menu: list) -> int:
    menu_width = 0
    title_width = len(title)
    for element in menu:
        if len(element) > menu_width:
            menu_width = len(element)
    return max(menu_width, title_width)


def get_column_width(contacts: dict, column: int) -> int:
    max_width = 0
    for contact in contacts.values():
        curr_column = len(contact.get_contact_data()[column])
        if curr_column > max_width:
            max_width = curr_column
    return max_width