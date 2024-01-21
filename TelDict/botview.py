import telebot
from telebot import types
import text
bot = telebot.TeleBot('5643059533:AAG-ZqfOi2ZP03UY0deu8QfYcwcqtLtWB0w')
 # t.me/AGR29_6bot.
@bot.message_handler(commands=['start'])
def main_menu_print(message): 
    mainkey=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for n, item in enumerate(text.main_menu):
         if n==0:
            print(item)
         else:
            mainkey.add(types.KeyboardButton(item))
    bot.send_message(message.from_user.id, text = text.main_menu_choice, reply_markup=mainkey)

def print_message(massage:str,user_id):
    bot.send_message(user_id, text=massage)

def show_contacts(p_book: dict[int,list[str]], error_message: str, user_id):
    if p_book:
        for n, contact in p_book.items():
            print_message(f"{n}. {contact[0]} {contact[1]} {contact[2]}", user_id)
    else:
        print_message(error_message, user_id)

def add_contact(message: list[str], user_id, contact: list[str] = None):
    contact=contact if contact else ['','','']
    for n, mes in enumerate(message):
        msg=print_message(mes,user_id)
        bot.register_next_step_handler(msg, input_str)
        field=input_str
        print(field)
        contact[n]=field if field else contact[n]
    return contact
def input_str(message):
    return message.text



      
       

bot.polling(none_stop=True, interval=0)
