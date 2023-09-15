import csv
from pathlib import *

# Функция для загрузки данных из файла
def load_contacts(filename):
    contacts = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

# Функция для сохранения данных в файл
def save_contacts(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Функция для добавления нового контакта
def add_contact(filename,contacts):
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")
    contact = [name, phone_number, email]
    contacts.append(contact)
    save_contacts(filename, contacts)
    print("Контакт успешно добавлен.")

# Функция для просмотра всех контактов
def view_contacts(contacts):
    print("Список контактов:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Имя: {contact[0]}, Телефон: {contact[1]}, Email: {contact[2]}")

# Функция для поиска контакта по имени
def search_contact(contacts):
    name = input("Введите имя для поиска: ")
    found_contacts = []
    for contact in contacts:
        if name.lower() in contact[0].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Результаты поиска:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Имя: {contact[0]}, Телефон: {contact[1]}, Email: {contact[2]}")
    else:
        print("Контакты не найдены.")

# Функция для удаления контакта
def delete_contact(contacts):
    try:
        index = int(input("Введите номер контакта для удаления: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Контакт {deleted_contact[0]} успешно удален.")
        else:
            print("Неверный номер контакта.")
    except ValueError:
        print("Неверный номер контакта.")

# Функция для изменения контакта
def edit_contact(contacts):
    index = int(input("Введите номер контакта для редактирования: ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        print("Текущая информация:")
        print(f"Имя: {contact[0]}, Телефон: {contact[1]}, Email: {contact[2]}")

        name = input("Введите новое имя (оставьте пустым, чтобы оставить без изменений): ")
        phone_number = input("Введите новый номер телефона (оставьте пустым, чтобы оставить без изменений): ")
        email = input("Введите новый адрес электронной почты (оставьте пустым, чтобы оставить без изменений): ")

        if name:
            contact[0] = name
        if phone_number:
            contact[1] = phone_number
        if email:
            contact[2] = email

        print("Контакт успешно изменен.")
    else:
        print("Неверный номер контакта.")

# Основной код приложения
def main():
    current_dir = Path.cwd()
    print(current_dir)

    filename = Path.cwd() / 'Task38' /'contacts.csv'
    contacts = load_contacts(filename)

    while True:
        print("\nТелефонный справочник:")
        print("1. Просмотр контактов")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Удалить контакт")
        print("5. Изменить контакт")
        print("6. Сохранить и выйти")

        choice = input("Выберите действие: ")
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(filename, contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            edit_contact(contacts)
        elif choice == "6":
            save_contacts(filename, contacts)
            print("Контакты успешно сохранены.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()