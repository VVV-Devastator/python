a = [int(x) for x in input("Введите урожайность грядки черники через пробел: ").split()]

max_berries = 0
for i in range(len(a)):
    berries = a[i] + a[(i - 1) % len(a)] + a[(i + 1) % len(a)]
    if berries > max_berries:
        max_berries = berries

print("Максимальное количество ягод, которое может быть собрано за один заход:", max_berries)