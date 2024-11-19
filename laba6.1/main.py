#В пассажирском поезде 9 вагонов. Выведите все возможные варианты рассадки в поезде 4 человек,
# при условии, что все они должны ехать в различных вагонах?
from itertools import combinations, permutations
import timeit
num_vagons= 9
num_passengers = 4

def algorithmically():
    position = 0
    for vagons_1 in range(9):
        for vagons_2 in range(9):
            if vagons_1 ==vagons_2:
                continue
            for vagons_3 in range(9):
                if vagons_1 == vagons_3 or vagons_2 == vagons_3:
                    continue
                for vagons_4 in range(9):
                    if vagons_1 == vagons_4 or vagons_2 == vagons_4 or vagons_3 == vagons_4:
                        continue
                    else:
                        position += 1
                        print(f"Пассажир_1 Вагон: {vagons_1}, Пассажир_2 Вагон: {vagons_2}, Пассажир_3 Вагон: {vagons_3}, Пассажир_4 Вагон: {vagons_4}")
    print(position)
    return
algorithmically()


def seating_arrangements(num_vagons, num_passengers):
    # Получаем все возможные комбинации вагонов
    vagons = range(1, num_vagons + 1)
    all_combinations = combinations(vagons, num_passengers)

    # Для каждой комбинации вагонов генерируем перестановки пассажиров
    arrangements = []
    for combo in all_combinations:
        for perm in permutations(range(1, num_passengers + 1)):
            arrangements.append((combo, perm))

    return arrangements


arrangements = seating_arrangements(num_vagons, num_passengers)

# Печатаем результаты
#for vagons, passengers in arrangements:
    #print(f"Вагоны: {vagons}, Пассажиры: {passengers}")
#print(len(arrangements))


time_func1 = timeit.timeit(lambda: algorithmically(), number=1)
print("algorithmically")
print(time_func1)
time_func2 = timeit.timeit(lambda: seating_arrangements(num_vagons, num_passengers), number=1)
print("function")
print(time_func2)

if time_func1>time_func2:
    print("Функционально программа быстрее")
else:
    print("Алгоритмически программа выполняется быстрее")


    #усложнённый вариант#################################################

