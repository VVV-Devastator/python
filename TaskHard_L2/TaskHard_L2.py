def count_digits(number):
    number = number.replace(',', '').replace('.', '')  # удаление запятых и точек
    return len(number)

number = input("Введите число: ")
digit_count = count_digits(number)
print("Количество цифр в числе:", digit_count)