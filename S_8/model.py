path = 'contacts.txt'
contacts = {}
ID = 0
FIRST_NAME = 1
LAST_NAME = 2
TEL = 3
COMMENT = 4
def load_contacts() -> list:
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def get_contacts():
    global contacts
    data = load_contacts()
    for contact in data:
        contact = contact.strip().split(';')
        contacts[int(contact[ID])] = [contact[FIRST_NAME],
                                      contact[LAST_NAME],
                                      contact[TEL],
                                      contact[COMMENT]]


def search_contact(search_data: str) -> dict:
    global contacts
    find_contacts = {}
    for contact in contacts:
        contact_data = str(' '.join(contacts[contact]))
        if search_data in contact_data:
            find_contacts[contact] = contacts[contact]
    return find_contacts


def add_new_contact(new_contact_data: list) -> bool:
    global contacts
    contacts_size = len(contacts)
    contacts[contacts_size + 1] = new_contact_data

    return True if contacts_size < len(contacts) else False


def change_contact(id: int, new_contact_data: list):
    global contacts
    contacts[id] = new_contact_data
    # TODO проверку на пустые строки
    return True


def delete_contact(id):
    global contacts
    contacts.__delitem__(id)

    return True


def save_contacts() -> bool:
    global contacts
    new_contacts = []
    for contact in contacts:
        new_contacts.append(f'{str(contact)};{";".join(contacts[contact])}')
    new_contacts = '\n'.join(new_contacts)
    print(new_contacts)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(new_contacts)
    return True