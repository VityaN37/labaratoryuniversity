#В пассажирском поезде 9 вагонов. Выведите все возможные варианты рассадки в поезде 4 человек,
# при условии, что все они должны ехать в различных вагонах?
from tkinter import *
from tkinter import ttk

root = Tk()

root.title("METANIT.COM")
root.geometry("250x200")

entry= ttk.Entry()
entry.pack(anchor=NW, padx=8, pady=8)

def show_message():
    label["text"] = entry.get()
    num_passengers = entry.get()
    print(num_passengers)

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()