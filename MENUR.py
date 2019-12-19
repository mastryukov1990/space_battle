from tkinter import Tk, Button

Game_mode = 0


def single():
    f1 = open('Game_mode.txt', 'w')
    f1.write('1')
    f1.close()
    root.destroy()

def versus():
    f1 = open('Game_mode.txt', 'w')
    f1.write('0')
    f1.close()
    root.destroy() 
    
def reference():
    g = 1 

class Menu():
    def __init__(self):
        
        self.b1 = Button(text = "Single Player", width = 20, command = single).pack()
        self.b2 = Button(text = "Versus Mode", width = 20, height = 3, command = versus).pack()
        self.b3 = Button(text = "Rules", width = 20, command = reference).pack()
    
    
    


root = Tk()
m = Menu()
root.mainloop()

print(Game_mode)

