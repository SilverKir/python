import text
import view
import model

def find_contact(phonebook: model.PhoneBook()):
    word = view.input_data(text.input_search_word)
    result = phonebook.find_contact(word)
    view.show_contacts(result, text.contacts_not_found(word))

def start_app():
    pb = model.PhoneBook()
    while True:
        choice = view.main_menu()
        match choice:
                case 1:
                    pb.open_file()
                    view.print_message(text.load_successful)
                case 2:
                    pb.save_file()
                    view.print_message(text.save_successful)
                case 3:
                    view.show_contacts(pb.phonebook,text.empty_phone_book)
                case 4:
                    contact=view.add_contact(text.new_contact)
                    pb.new_contact(contact)
                    view.print_message(text.new_contact_added_successful(contact[0]))
                case 5:
                    find_contact(pb)
                case 6:
                    find_contact(pb)
                    c_id=int(view.input_data(text.input_id_change_contact))
                    c_contact=view.add_contact(text.change_contact, pb.phonebook[c_id])
                    pb.change_contact(c_id,c_contact)
                    view.print_message(text.contact_changed_successful(c_contact[0]))
                case 7:
                    find_contact(pb)
                    c_id = int(view.input_data(text.input_id_delete_contact))
                    name= pb.delete_contact(c_id)[0]
                    view.print_message(text.contact_deleted_successful(name))
                case 8:
                    view.print_message(text.good_bay)
                    break

