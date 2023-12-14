import json
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

def view_notes():
    if not notes:
        print("Нет доступных заметок.")
        return

    print("Список заметок:")
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['message']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print()

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            note["title"] = title
            note["message"] = message
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

# Загрузка существующих заметок
notes = load_notes()

# Основной цикл приложения
while True:
    command = input("Введите команду (add, view, edit, delete, exit): ")

    if command == "add":
        add_note()
    elif command == "view":
        view_notes()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "exit":
        break
    else:
        print("Неверная команда. Попробуйте еще раз.")