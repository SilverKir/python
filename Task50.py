# Задача №49. Общее обсуждение Создать телефонный справочник

# Функции (можно вынести в отдельный файл) можно доработать что бы словарь не ограничивалс 3 строками
def print_menu(list_print, argument=None):
        global contact_id
        print(list_print[0][0])
        contact_id = argument #Индекс выбранного адреса
        if list_print[0][1]: exec(list_print[0][1]) # если есть команда у меню
        [print(f"{i}. {list_print[i][0]}") for i in range(len(list_print)) if i>0]
        while True:
                menu_item = input("Введите нужный номер: ")
                try:
                        menu_item=int(menu_item)
                        while menu_item not in range(1,len(list_print)):
                                menu_item = int(input(f"Ваше значение не верно, введите число в диапазоне от 1 до {len(list_print) - 1}: "))
                        else: return list_print[int(menu_item)][1]
                except ValueError:
                        print(f"Ваше значение не верно, введите число в диапазоне от 1 до {len(list_print) - 1}: ")

def save_file(file_name, contact_list):
        with open(file_name,"w",encoding='UTF-8') as file:
                [file.write(f"{string[0]};{string[1]};{string[2]}\n") for string in contact_list]
        file.close()
        print(f"Данные успешно сохранены в файл {file_name}")
        
def open_file(file_name):
        tel_cont = []
        try:
                with open(file_name,"r", encoding='UTF-8') as file:
                        data_tel=file.readlines()
                        [tel_cont.append(tel_item.split(";")) for tel_item in data_tel]
                        for i in range(len(tel_cont)):
                                tel_cont[i][-1]=tel_cont[i][-1].replace("\n","")
                file.close()
        except IOError:
                file=open(file_name, "w+")
                file.close()
        return tel_cont

def new_contact(list_contacts):
        new_cont=[input("Введите имя контакта: "),input("Введите телефон контакта: "), input("Введите ник контакта: ")]
        list_contacts.append(new_cont)
        print(f"Контакт:\n Имя:{new_cont[0]} Телефон:{new_cont[1]} Ник:{new_cont[2]} \n добавлен, нажмите Enter для входа в главное меню.")
        input()
        exec(print_menu(main_menu))

def print_contacts(list_contacts,param=1):
        if len(list_contacts)==0:
                print("Телефонная книга пуста: Занесите пожалуйста первый контакт:")
                new_contact(list_contacts)
        else:
                [print(f"{i+1}. Имя:{list_contacts[i][0]} Телефон:{list_contacts[i][1]} Ник:{list_contacts[i][2]}") for i in range(len(list_contacts))]
                if param==1:
                        input()
                        exec(print_menu(main_menu))

def print_contact_item(list_contacts,contact_id):
        print(f"Контакт Имя:{list_contacts[contact_id][0]} Телефон:{list_contacts[contact_id][1]} Ник:{list_contacts[contact_id][2]}")

def edit_contact_item(list_contacts,contact_id):
        list_contacts[contact_id][0]=input(f"Измените имя контакта {list_contacts[contact_id][0]}: " )
        list_contacts[contact_id][1] = input(f"Измените телефон контакта {list_contacts[contact_id][1]}: ")
        list_contacts[contact_id][2] = input(f"Измените ник контакта {list_contacts[contact_id][2]}: ")
        print_contact_item(list_contacts, contact_id)
        input(f" добавлен, нажмите Enter для входа в главное меню.")
        exec(print_menu(main_menu))

def del_contact_item(list_contacts,contact_id,type_del=1):
        if type_del==1: return exec(print_menu(menu_del, contact_id))
        else:
                print_contact_item(list_contacts, contact_id)
                list_contacts.pop(contact_id)
                input(f" удалeн, нажмите Enter для просмотра актуального списка контактов.")
                print_contacts(tel_contact)

def find_contact(list_contacts, find_type):
        if len(list_contacts)==0:
                print("Телефонная книга пуста: Занесите пожалуйста первый контакт:")
                new_contact(list_contacts)
        else:
                if find_type==1: # Поиск по индексу
                        print_contacts(list_contacts, 2)
                        menu_item = int(input("Введите нужный номер: "))
                        while menu_item not in range(1, len(list_contacts)+1):
                                menu_item = int(input(f"Ваше значение не верно, введите число в диапазоне от 1 до {len(list_contacts)}: "))
                        else:
                                return exec(print_menu(menu_edit, int(menu_item) - 1))
                else:
                        find_criterion=input(f"Введите {list_fields[find_type-2]} для поиска:")
                        for item in list_contacts:
                                if find_criterion in item[find_type-2]:
                                      return exec(print_menu(menu_edit, list_contacts.index(item)))
                print("К сожалению, поиск не увенчался успехом, нажмите Enter для выхода в главное меню")
                input()
                exec(print_menu(main_menu))

#   Программа, задает меню и тд.
menu_del=[("           УДАЛЕНИЕ \nВы точно хотите удалить запись: ", "print_contact_item(tel_contact,contact_id)"), ("NO", "exec(print_menu(list_edit,contact_id))"), ("YES", "del_contact_item(tel_contact,contact_id,2)"), ("Вернуться в главное меню", "exec(print_menu(main_menu))")]
menu_edit=[("           РЕДАКТИРОВАНИЕ \nДействия с выбранной записью", "print_contact_item(tel_contact,contact_id)"), ("Edit", "edit_contact_item(tel_contact,contact_id)"), ("Delete", "del_contact_item(tel_contact,contact_id)"), ("Вернуться в главное меню", "exec(print_menu(main_menu))")]
menu_exit=[("           ВЫХОД \nСохранить изменения?",""),("YES","save_file(file_name,tel_contact)"),("NO","print("'"До свидания! Вышли без сохранения."'")"),("Вернуться в главное меню","exec(print_menu(main_menu))" )]
main_menu=[("           ГЛАВНОЕ МЕНЮ \nВыберете Ваше действие:",""),("Show contacts","print_contacts(tel_contact)"),("Create contact","new_contact(tel_contact)"),("Find (Edit, Delete)","exec(print_menu(menu_find))"),("Exit","exec(print_menu(menu_exit))")]
menu_find=[("           ПОИСК \n Выберете параметры поиска",""),("By index","find_contact(tel_contact, 1)"),("By name","find_contact(tel_contact, 2)"),("By tel","find_contact(tel_contact, 3)"),("By nick","find_contact(tel_contact, 4)")]

list_fields=["имя", "телефон", "ник"] # названия полей
file_name='tel_directory.txt' # файл словар
tel_contact = open_file(file_name) # занесение данных в переменную
exec(print_menu(main_menu)) # запуск основного меню
