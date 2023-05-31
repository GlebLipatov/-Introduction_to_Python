import PhoneBook
import view
import text

is_exit = False


def back_to_main_menu(choice: int) -> bool:
    return True if choice == 2 else False


def start():
    global is_exit
    pb = PhoneBook.PhoneBook()
    contacts = pb.phone_book

    while not is_exit:
        user_choice = view.show_menu(text.main_menu, text.title_main_menu)

        match user_choice:
            case 1:
                inner_choice = view.show_contacts(contacts)
                is_exit = back_to_main_menu(inner_choice)
            case 2:
                search_data = view.show_search(text.title_search_menu)
                find_contacts = pb.search(search_data)
                inner_choice = view.show_contacts(find_contacts)
                is_exit = back_to_main_menu(inner_choice)
            case 3:
                new_contact_data = view.show_menu_add(text.title_add_contact)
                pb.add(new_contact_data)
                inner_choice = view.show_successfully_message(text.contact_added)
                is_exit = back_to_main_menu(inner_choice)
            case 4:
                search_data = view.show_search(text.title_contact_data_to_change)
                find_contacts = pb.search(search_data)
                id = view.show_contacts_to_change(find_contacts)
                changed_contact_data = view.show_menu_add(text.title_enter_new_data)
                contact = contacts[id]
                pb.change(contact, changed_contact_data)
                inner_choice = view.show_successfully_message(text.contact_changed)
                is_exit = back_to_main_menu(inner_choice)
            case 5:
                search_data = view.show_search(text.title_contact_data_to_delete)
                find_contacts = pb.search(search_data)
                id = view.show_contacts_to_change(find_contacts)
                pb.delete(id)
                inner_choice = view.show_successfully_message(text.contact_deleted)
                is_exit = back_to_main_menu(inner_choice)
            case 6:
                pb.save()
                inner_choice = view.show_successfully_message(text.contacts_saved)
                is_exit = back_to_main_menu(inner_choice)
            case 7:
                is_exit = True
