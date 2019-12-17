from tkinter import *

root = Tk()
root.title("settings")

Label(text="Имя:").grid(row=0, column=0)
table_name = Entry(width=30)
table_name.grid(row=0, column=1, columnspan=3)

Label(text="Mob_size:").grid(row=1, column=0)
table_column = Spinbox(width=7, from_=1, to=50)
table_column.grid(row=1, column=1)
Label(text="number:").grid(row=1, column=2)
table_row = Spinbox(width=10, from_=1, to=100)
table_row.grid(row=0, column=4)

Button(text="Назад").grid(row=2, column=0)
Button(text="Применить").grid(row=2, column=2)
table_row.grid(row=2, column=3)

root.mainloop()