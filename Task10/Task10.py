
def min_flips(coins):
    heads = coins.count('H')
    tails = coins.count('T')
    return min(heads, tails)

# Пример использования
coins = ['H', 'T', 'T', 'H', 'H', 'H', 'H', 'T']
min_flips_needed = min_flips(coins)
print("Минимальное количество переворотов:", min_flips_needed)