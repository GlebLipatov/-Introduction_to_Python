import model
import view
import text

is_exit = False

def back_to_main_menu(choice: int) -> bool:
    return True if choice == 2 else False


def start():
    global is_exit
    model.get_contacts()
    contacts = model.contacts

    while not is_exit:
        user_choice = view.show_menu(text.main_menu, text.title_main_menu)

        match user_choice:
            case 1:
                inner_choice = view.show_contacts(contacts)
                is_exit = back_to_main_menu(inner_choice)
            case 2:
                search_data = view.show_search_contact(text.title_search_menu)
                find_contacts = model.search_contact(search_data)
                inner_choice = view.show_contacts(find_contacts)
                is_exit = back_to_main_menu(inner_choice)
            case 3:
                new_contact_data = view.show_add_contact(text.title_add_contact)
                is_add = model.add_new_contact(new_contact_data)
                inner_choice = view.show_successfully_message(is_add, text.contact_added)
                is_exit = back_to_main_menu(inner_choice)
            case 4:
                search_data = view.show_search_contact(text.title_contact_data_to_change)
                find_contacts = model.search_contact(search_data)
                id = view.show_contacts_to_change(find_contacts)
                changed_contact_data = view.show_add_contact(text.title_enter_new_data)
                is_changed = model.change_contact(id, changed_contact_data)
                inner_choice = view.show_successfully_message(is_changed, text.contact_changed)
                is_exit = back_to_main_menu(inner_choice)
            case 5:
                search_data = view.show_search_contact(text.title_contact_data_to_delete)
                find_contacts = model.search_contact(search_data)
                id = view.show_contacts_to_change(find_contacts)
                is_delete = model.delete_contact(id)
                inner_choice = view.show_successfully_message(is_delete, text.contact_deleted)
                is_exit = back_to_main_menu(inner_choice)
            case 6:
                is_save = model.save_contacts()
                inner_choice = view.show_successfully_message(is_save, text.contacts_saved)
                is_exit = back_to_main_menu(inner_choice)
            case 7:
                is_exit = True