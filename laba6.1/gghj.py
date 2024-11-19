from itertools import combinations, permutations
import timeit
num_passengers = 4

num_vagons=[1,2,3,4,5,6,7,8,9]
new_vagon=[]
t=0
for i in num_vagons:
    if i %2 !=0:
        new_vagon.append(i)
print(new_vagon)

num_vagons1=len(new_vagon)
def algorithmically(position):

    for vagons_1 in range(num_vagons1):
        for vagons_2 in range(num_vagons1):
            if vagons_1 ==vagons_2:
                continue
            for vagons_3 in range(num_vagons1):
                if vagons_1 == vagons_3 or vagons_2 == vagons_3:
                    continue
                for vagons_4 in range(num_vagons1):
                    if vagons_1 == vagons_4 or vagons_2 == vagons_4 or vagons_3 == vagons_4:
                        continue
                    else:
                        position += 1
                        print(f"Пассажир_1 Вагон: {vagons_1}, Пассажир_2 Вагон: {vagons_2}, Пассажир_3 Вагон: {vagons_3}, Пассажир_4 Вагон: {vagons_4}")
    print(f"{position}")
    return position
algorithmically(0)


def seating_arrangements(num_vagons1, num_passengers):
    # Получаем все возможные комбинации вагонов
    vagons = range(1, num_vagons1 + 1)
    all_combinations = combinations(vagons, num_passengers)

    # Для каждой комбинации вагонов генерируем перестановки пассажиров
    arrangements = []
    for combo in all_combinations:
        for perm in permutations(range(1, num_passengers + 1)):
            arrangements.append((combo, perm))

    return arrangements


arrangements = seating_arrangements(num_vagons1, num_passengers)




time_func1 = timeit.timeit(lambda: algorithmically(0), number=1)
print("algorithmically")
print(time_func1)
time_func2 = timeit.timeit(lambda: seating_arrangements(num_vagons1, num_passengers), number=1)
print("function")
print(time_func2)

if time_func1>time_func2:
    print("Функционально программа быстрее")
else:
    print("Алгоритмически программа выполняется быстрее")

# Печатаем результаты
print(len(arrangements))
