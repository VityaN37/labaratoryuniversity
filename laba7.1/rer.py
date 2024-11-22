from itertools import combinations, permutations
from tkinter import *
from tkinter import ttk
import tkinter as tk
import timeit
num_vagons=[]

root = Tk()

root.title("Train")
root.geometry("250x200")

label = ttk.Label(text="Введите количество пассажиров по заданию")
label.pack()

entry= ttk.Entry()
entry.pack(anchor=NW, padx=8, pady=8)



count_vagon=9#int(input())

for i in range(count_vagon+1):
    num_vagons.append(i)

new_vagon=[]
for i in num_vagons:
    if i %2 !=0:
        new_vagon.append(i)
print(new_vagon)



def seating_arrangements():
    # Получаем все возможные комбинации вагонов
    e = entry.get()
    num_passengers=int(e)
    new_vagon=[1,3,5,7,9]

    all_combinations = combinations(new_vagon, num_passengers)

    # Для каждой комбинации вагонов генерируем перестановки пассажиров
    arrangements = []
    for combo in all_combinations:
        for perm in permutations(range(1, num_passengers + 1)):
            arrangements.append((combo, perm))

    # Печатаем результаты
    for vagons, passengers in arrangements:
        print(f"Вагоны: {vagons}, Пассажиры: {passengers}")
    print(len(arrangements))
    return arrangements




#time_func2 = timeit.timeit(lambda: seating_arrangements(num_vagons1, num_passengers), number=1)
#print("function")
#print(time_func2)


btn = ttk.Button(text="Click", command=seating_arrangements(new_vagon))
btn.pack(anchor=N, padx=6, pady=6)



root.mainloop()

