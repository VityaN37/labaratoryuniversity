from itertools import combinations, permutations
from tkinter import *
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText


def seating_arrangements():
    # Получаем все возможные комбинации вагонов
    num_passengers = int(entry.get())
    num_vagons = []
    count_vagon=0
    count_vagon =int(entry_1.get())

    for i in range(count_vagon + 1):
        num_vagons.append(i)

    new_vagon = []
    for i in num_vagons:
        if i % 2 != 0:
            new_vagon.append(i)

    all_combinations = combinations(new_vagon, num_passengers)
    result_max = 0

    # Для каждой комбинации вагонов генерируем перестановки пассажиров
    arrangements = []
    for combo in all_combinations:
        for perm in permutations(range(1, num_passengers + 1)):
            arrangements.append((combo, perm))

    # Печатаем результаты
    for vagons, passengers in arrangements:
        result = 0
        result = passengers[0] * vagons[0]+passengers[1] * vagons[1]+passengers[2] * vagons[2]+passengers[3] * vagons[3]
        if result > result_max:
            h=[]
            h.append((vagons,passengers))
            result_max = result
    for vagons, passengers in h:
        text.insert(1.0,f"\nВагоны: {vagons}, Пассажиры: {passengers}\n")
    text.insert(1.0,f"\nСамая большая сумма: {result_max}")
    return arrangements

root = Tk()

root.title("Tkinter")
root.geometry("500x300")
root.resizable(width=False,height=False)
label = Label(text="Введите количество пассажиров по заданию", font=("Arial",12))
label.pack()
label.place(x=1, y=1)
label_3 = Label(text="Введите количество вагонов по заданию",font=("Arial",12))
label_3.pack()
label_3.place(x=1, y=30)

entry= Entry()
entry.pack()
entry.place(x=340,y=3)
entry_1= Entry()
entry_1.pack()
entry_1.place(x=340,y=30)
btn = Button(text="Начать подсчёт", command=seating_arrangements)
btn.pack()
btn.place(x=200, y=80)


text =ScrolledText(root,width=70,height=10)
text.pack(side=BOTTOM)


label_1=Label(background="white")
label_1.pack()
label_1.place(x=5, y=140)
label_2 = Label(background="white")
label_2.pack()
label_2.place(x=5, y=160)

root.mainloop()

