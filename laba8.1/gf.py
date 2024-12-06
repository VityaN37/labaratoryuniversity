import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class CreditAgreement:
    def __init__(self, contract_id, amount, manager):
        self.contract_id = contract_id
        self.amount = float(amount)
        self.manager = manager

    @staticmethod
    def read_agreements_from_file(filename):
        agreements = []
        try:
            with open("test.txt", 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) != 3:
                        raise ValueError(f"Неправильный формат строки: {line.strip()}")
                    contract_id, amount, manager = parts
                    agreements.append(CreditAgreement(contract_id, amount, manager))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прочитать файл: {str(e)}")
        return agreements

    @staticmethod
    def segment_by_amount(agreements):
        small = [ag for ag in agreements if ag.amount < 10000]
        medium = [ag for ag in agreements if 10000 <= ag.amount < 50000]
        large = [ag for ag in agreements if ag.amount >= 50000]
        return len(small), len(medium), len(large)

    @staticmethod
    def segment_by_manager(agreements):
        manager_count = {}
        for ag in agreements:
            if ag.manager not in manager_count:
                manager_count[ag.manager] = 0
            manager_count[ag.manager] += 1
        return manager_count

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

        self.agreements = []

        self.load_button = tk.Button(root, text="Загрузить данные", command=self.load_data)
        self.load_button.pack()

        self.segment_amount_button = tk.Button(root, text="Сегментировать по суммам", command=self.segment_by_amount)
        self.segment_amount_button.pack()

        self.segment_manager_button = tk.Button(root, text="Сегментировать по менеджерам", command=self.segment_by_manager)
        self.segment_manager_button.pack()

    def load_data(self):
        self.agreements = CreditAgreement.read_agreements_from_file("contracts.txt")
        if self.agreements:
            messagebox.showinfo("Информация", f"Загружено {len(self.agreements)} договоров.")

    def segment_by_amount(self):
        if not self.agreements:
            messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
            return
        small_count, medium_count, large_count = CreditAgreement.segment_by_amount(self.agreements)
        sizes = {'Мелкие': small_count, 'Средние': medium_count, 'Крупные': large_count}
        CreditAgreement.plot_pie_chart(sizes, "Сегментация по суммам")

    def segment_by_manager(self):
        if not self.agreements:
            messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
            return
        manager_data = CreditAgreement.segment_by_manager(self.agreements)
        CreditAgreement.plot_pie_chart(manager_data, "Сегментация по менеджерам")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
