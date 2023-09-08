import random

def find_indices_in_range(lst, minimum, maximum):
    indices = []
    for i, value in enumerate(lst):
        if minimum <= value <= maximum:
            indices.append(i)
    return indices

def generate_random_list(length, minimum, maximum):
    lst = []
    for _ in range(length):
        value = random.randint(minimum, maximum)
        lst.append(value)
    return lst


length = 6
minimum = 33
maximum = 200
random_list = generate_random_list(length, minimum, maximum)

minimum1 = 50
maximum2 = 100


# Вызов функции и вывод результата
indices = find_indices_in_range(random_list, minimum1, maximum2)
print("Список:", random_list)
print("Ответ:", indices)