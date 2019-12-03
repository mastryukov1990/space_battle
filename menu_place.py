from tkinter import *
m = 'm'

l_con = ['size','number:','fire:', 'on:','touch','Number of strikes']
class Settings:
    def __init__(self,l_con):
        self.labels ={}
        self.k = 0
        self.x = 0.1
        self.label = 1
        self.spinbox = 2
        self.width = 0.2
        self.hieght = 0.1
        self.y = 0
        self.l_con = l_con
        self.checkbutton = 3
        
       
        for i in self.l_con:
            self.labels.update({i:{}})
        for i in self.labels:
            self.y = 0.1 + self.k/20
            self.labels[i].update({self.label:{'x':self.x,'width':self.width,'hieght': self.hieght},self.spinbox:{}})
            self.labels[i][self.label].update({'y':self.y})
            print(self.labels[i])
            self.k = self.k+ 1
        self.spinboxes ={self.l_con[0]:{},self.l_con[1]:{}}
        for t in self.spinboxes:
            self.labels[t].update({self.spinbox:{}})
            self.labels[t][self.spinbox].update({'y': self.labels[t][self.label]['y'],'x':self.labels[t][self.label]['x']+ self.width} )
            print(self.labels[t])
        self.checkbuttons = {self.l_con[2]:{},self.l_con[3]:{}}
        for t in self.checkbuttons:
            self.labels[t].update({self.checkbutton:{}})
            self.labels[t][self.checkbutton].update({'y': self.labels[t][self.label]['y'],'x':self.labels[t][self.label]['x']+2* self.width} )
            print(self.labels[t])

    
    
        b = Button(text ='Push',bg='red').place(relx=0.4, rely=0.8, relwidth = 0.2, relheight =0.05)
        for i in self.l_con:
            l = self.labels[i][self.label]
            Label(text = i, bg = 'white').place(relx =l['x'], rely = l['y'],relwidth =l['width'])
            if self.labels[i][self.spinbox]:
                s = self.labels[i][self.spinbox]
                Spinbox(bg = 'yellow',from_=1, to = 20000).place(relx = s['x'], rely = s['y'], relwidth = 0.2, relheight = 0.05)
                
            print(self.labels[i][1])
root = Tk()

root.title("settings")
root.geometry('500x500')
menu = Settings(l_con)
root.mainloop()