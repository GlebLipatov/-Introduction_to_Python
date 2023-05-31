import Contact


class PhoneBook:
    ID = 0
    FIRST_NAME = 1
    LAST_NAME = 2
    PHONE_NUMBER = 3
    COMMENT = 4

    def __init__(self, path: str = 'contacts.txt'):
        self.phone_book = {}
        self.id_next = 0
        self.path = path
        self.get_contacts()

    def load(self) -> list:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        return data

    def get_contacts(self):
        data = self.load()
        for contact in data:
            contact = contact.strip().split(';')
            self.phone_book[int(contact[self.ID])] = Contact.Contact(contact[self.ID],
                                                                     contact[self.FIRST_NAME],
                                                                     contact[self.LAST_NAME],
                                                                     contact[self.PHONE_NUMBER],
                                                                     contact[self.COMMENT])
        self.id_next = len(self.phone_book) + 1
        return self.phone_book

    def search(self, search_data: str) -> dict:
        find_contacts = {}
        for contact in self.phone_book.values():
            contact_data = ' '.join(contact.get_contact_data())
            if search_data in contact_data:
                find_contacts[int(contact.id)] = contact
        return find_contacts

    def add(self, new_contact_data: list):
        self.phone_book[self.id_next] = Contact.Contact(self.id_next,
                                                        new_contact_data[self.FIRST_NAME - 1],
                                                        new_contact_data[self.LAST_NAME - 1],
                                                        new_contact_data[self.PHONE_NUMBER - 1],
                                                        new_contact_data[self.COMMENT - 1])
        self.id_next += 1

    def change(self, contact: Contact, new_data: list):
        # у индексов вычитаю 1 потому что new_data начинается с first_data, а не с id
        if new_data[self.FIRST_NAME - 1] != '':
            contact.set_first_name(new_data[self.FIRST_NAME - 1])
        if new_data[self.LAST_NAME - 1] != '':
            contact.set_last_name(new_data[self.LAST_NAME - 1])
        if new_data[self.PHONE_NUMBER - 1] != '':
            contact.set_phone_number(new_data[self.PHONE_NUMBER - 1])
        if new_data[self.COMMENT - 1] != '':
            contact.set_comment(new_data[self.COMMENT - 1])

    def delete(self, id):
        self.phone_book.__delitem__(id)

    def save(self):
        new_phone_book = ''
        for contact in self.phone_book.values():
            new_phone_book += contact.get_data_to_save()
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(new_phone_book)