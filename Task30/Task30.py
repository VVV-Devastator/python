def generate_arithmetic_progression():
    a1 = int(input("Введите первый элемент прогрессии (a1): "))
    d = int(input("Введите разность прогрессии (d): "))
    n = int(input("Введите количество элементов прогрессии (n): "))

    progression = []
    for i in range(n):
        an = a1 + i * d
        progression.append(an)

    return progression

progression = generate_arithmetic_progression()
print("Арифметическая прогрессия:", progression)