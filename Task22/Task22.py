n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set_1 = set()
set_2 = set()

# Ввод элементов первого множества
print("Введите элементы первого множества:")
for _ in range(n):
    element = int(input())
    set_1.add(element)

# Ввод элементов второго множества
print("Введите элементы второго множества:")
for _ in range(m):
    element = int(input())
    set_2.add(element)

# Находим пересечение множеств
intersection = sorted(set_1.intersection(set_2))

# Выводим результат
print("Числа, встречающиеся в обоих множествах:")
for number in intersection:
    print(number)