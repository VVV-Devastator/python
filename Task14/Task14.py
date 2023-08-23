def powers_of_two(N):
    k = 0
    power_of_two = 1
    while power_of_two <= N:
        print(power_of_two)
        k += 1
        power_of_two = 2 ** k

N = int(input("Введите  число: "))
powers_of_two(N)