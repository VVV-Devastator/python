def check_rhythm(poem):
    lines = poem.split()  
    syllables_count = []  

    for line in lines:
        words = line.split('-')  # Разделение строки на слова
        syllables = sum([sum(1 for char in word if char in 'аеёиоуыэюя') for word in words])
        syllables_count.append(syllables)

    if len(set(syllables_count)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"


poem = input("Введите стихотворение Винни-Пуха: ")


result = check_rhythm(poem)
print(result)