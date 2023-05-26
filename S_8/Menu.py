import Print_menu
import Phone_book

print_m = Print_menu.print_menu
main_menu = Print_menu.main_menu
print_contact = Print_menu.print_contacts
contacts = Phone_book.contacts

def start():
    print_m(main_menu)
    input_from_user = input()

    while(not input_from_user.isdigit() or int(input_from_user) > len(main_menu) - 3):
        print_m(main_menu)
        print(f'\n{Print_menu.alert()} {len(main_menu) - 3}.')
        input_from_user = input()

    input_from_user = int(input_from_user)

    if (input_from_user == 1): # Показать все контакты.
        print_contact(contacts)
        start()
    elif (input_from_user == 2): # Найти контакт.
        Print_menu.find()
        data = Phone_book.get_contact(contacts, input())
        if len(data) > 0:
            print_contact(data)
        else:
            Print_menu.not_found()
        start()
    elif (input_from_user == 3): # Добавить контакт.
        Phone_book.add_contact()
        start()
    elif (input_from_user == 4): # Изменить контакт
         Print_menu.find()
         Phone_book.change_contact()
         start()
    elif (input_from_user == 5): # Удалить контакт
        Print_menu.find()
        Phone_book.delete_contact()
        start()
    elif (input_from_user == 6): # Сохранить изменения.
        Phone_book.save()
        start()
    elif (input_from_user == 0): # Выход
        Print_menu.goodbye()
        return False