import text
import view
import model
import botview
import telebot
bot = telebot.TeleBot('5643059533:AAG-ZqfOi2ZP03UY0deu8QfYcwcqtLtWB0w')
pb = model.PhoneBook()

def find_contact(phonebook: model.PhoneBook()):
    word = view.input_data(text.input_search_word)
    result = phonebook.find_contact(word)
    view.show_contacts(result, text.contacts_not_found(word))

@bot.message_handler(content_types=['text'])
def start_app(message):
    if (message.text in text.main_menu):
        choice = text.main_menu.index(message.text)
        user_id = message.from_user.id
        match choice:
                case 1:
                    pb.open_file()
                    botview.print_message(text.load_successful,user_id)
                    view.print_message(text.load_successful)
                case 2:
                    pb.save_file()
                    botview.print_message(text.save_successful,user_id)
                    view.print_message(text.save_successful)
                case 3:
                    botview.show_contacts(pb.phonebook, text.empty_phone_book, user_id)
                    view.show_contacts(pb.phonebook, text.empty_phone_book)
                case 4:
                    contact=botview.add_contact(text.new_contact, user_id)
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
                    
bot.polling(none_stop=True, interval=0)
