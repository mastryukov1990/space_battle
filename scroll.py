from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

l = Label(root, yscrollcommand = scrollbar.set )


l.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = l.yview )

mainloop()