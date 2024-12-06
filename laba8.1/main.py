#Объекты – кредитные договоры Функции:
#сегментация полного списка договоров по суммам (мелкие, средние,крупные)
#визуализация предыдущей функции в форме круговой диаграммы
#сегментация полного списка договоров по менеджерам
#визуализация предыдущей функции в форме круговой диаграммы
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt
import self as self


class Contract:
    def __init__(self, sum_, name_contract,person_name):
        self.sum_ = float(sum_)
        self.name_contract = name_contract
        self.person_name = person_name

    @staticmethod
    def segment_by_amount(all_contract):
        small = [ct for ct in all_contract if ct.sum_ < 10000]
        medium = [ct for ct in all_contract if 10000 <= ct.sum_ < 50000]
        large = [ct for ct in all_contract if ct.sum_ >= 50000]
        return len(small), len(medium), len(large)

    @staticmethod
    def segment_by_manager(all_contract):
        manager_count = {}
        for ct in all_contract:
            if ct.person_name not in manager_count:
                manager_count[ct.person_name] = 0
            manager_count[ct.person_name] += 1
        print(manager_count)
        return manager_count

    def read(self):
        valid_managers = ["Johnson", "Bob", "Brown", "David", "Eva"]
        all_contract = []
        try:
            with open('test.txt', 'r') as file:

                for contract in file:
                    parts = contract.strip().split(',')
                    if len(parts) != 3:
                        raise ValueError(
                            f"Неправильный формат строки: {contract} \nСтрока должно выглядеть в формате: \nsum_, name_contract,person_name ")
                    sum_, name_contract, person_name = parts
                    if person_name not in valid_managers:
                        raise ValueError("Имя менеджера должно быть одним из следующих: " + ", ".join(valid_managers))
                    all_contract.append(Contract(sum_, name_contract, person_name))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прочитать файл: {str(e)}")
        return all_contract

    @staticmethod
    def plot_pie_chart(data, title):
        labels = data.keys()
        sizes = data.values()
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(title)
        plt.show()


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Кредитные договоры")

        self.all_contract = []

        self.load_button = Button(root, text="Загрузить данные", command=self.load_data)
        self.load_button.pack()

        self.segment_amount_button = Button(root, text="Сегментировать по суммам", command=self.segment_by_amount)
        self.segment_amount_button.pack()

        self.segment_manager_button = Button(root, text="Сегментировать по менеджерам", command=self.segment_by_manager)
        self.segment_manager_button.pack()

    def load_data(self):
        self.all_contract= Contract.read("test.txt")
        if self.all_contract:
            messagebox.showinfo("Информация", f"Загружено {len(self.all_contract)} договоров.")

    def segment_by_amount(self):
        if not self.all_contract:
            messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
            return
        small_count, medium_count, large_count = Contract.segment_by_amount(self.all_contract)
        sizes = {'Мелкие': small_count, 'Средние': medium_count, 'Крупные': large_count}
        Contract.plot_pie_chart(sizes, "Сегментация по суммам")

    def segment_by_manager(self):
        if not self.all_contract:
            messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
            return
        manager_data = Contract.segment_by_manager(self.all_contract)
        Contract.plot_pie_chart(manager_data, "Сегментация по менеджерам")


root = Tk()
root.title("Кредитные договоры")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 300  # смещение от середины
h = h - 350
root.geometry(f'500x300+{w}+{h}')
root.resizable(width=False, height=False)
app = App(root)
root.mainloop()







btn = Button(text="Загрузить данные", command=read)
btn.pack()
btn.place(x=200, y=50)

btn = Button(text="Сегментировать по суммам", command=Contract.segment_by_amount)
btn.pack()
btn.place(x=170, y=90)

btn = Button(text="Сегментировать по менеджерам", command=Contract.segment_by_manager)
btn.pack()
btn.place(x=160, y=140)
root.mainloop()