import Print_menu

path = 'contacts.txt'
file = open(path, 'r', encoding='utf-8')
FIRST_NAME = 0
LAST_NAME = 1
TEL = 2

def get_contacts():
    data = {}
    first_name = ''
    last_name = ''
    full_name = ''
    tel = ''
    id = 0

    for line in file:
        line = str(line)
        if line.startswith('id:'):
            id = int(line.split(':')[1].strip('\n'))
        elif line.startswith('first name:'):
            first_name = line.split(':')[1].strip('\n').lower()
        elif line.startswith('last name:'):
            last_name = line.split(':')[1].strip('\n').lower()
        elif line.startswith('tel:'):
            tel = line.split(':')[1].strip('\n')
        elif line.startswith('#'):
            info = [first_name, last_name, tel]
            data[id] = info
    return data


contacts = get_contacts()


def get_contact(input_from_user):
    FIRST_NAME = 0
    LAST_NAME = 1
    TEL = 2
    find_contacts = {}
    for contact in contacts:
        id = int(contact)
        first_name = contacts[contact][FIRST_NAME]
        last_name = contacts[contact][LAST_NAME]
        tel = contacts[contact][TEL]
        info_formated = f'{tel} {first_name} {last_name}'

        if info_formated.__contains__(input_from_user.lower()):
            info = [first_name, last_name, tel]
            find_contacts[id] = info
    return find_contacts


def add_contact():
    Print_menu.input_first_name()
    first_name = input()
    Print_menu.input_last_name()
    last_name = input()
    Print_menu.input_tel_number()
    tel = input()
    id = len(contacts) + 1
    contacts[id] = [first_name, last_name, tel]


def change_contact():
    input_form_user = str(input())
    data = get_contact(input_form_user)
    Print_menu.print_contacts_change(data)
    current_contact = int(input())
    Print_menu.what_change()
    point = int(input()) - 1
    if point == 0:
        Print_menu.input_first_name()
        contacts[current_contact][point] = input().lower()
    elif point == 1:
        Print_menu.input_last_name()
        contacts[current_contact][point] = input().lower()
    elif point == 2:
        Print_menu.input_tel_number()
        contacts[current_contact][point] = input()


def delete_contact():
    input_form_user = input()
    Print_menu.print_contacts_change(get_contact(input_form_user))
    input_id = int(input())
    contacts.__delitem__(input_id)


def save():
    file = open(path, 'w', encoding='utf-8')
    for contact in contacts:
        id = contact
        first_name = contacts[contact][FIRST_NAME]
        last_name = contacts[contact][LAST_NAME]
        tel = contacts[contact][TEL]
        file.write(f'id:{id}\n')
        file.write(f'first name:{first_name}\n')
        file.write(f'last name:{last_name}\n')
        file.write(f'tel:{tel}\n')
        file.write(f'#\n')

    file.close()