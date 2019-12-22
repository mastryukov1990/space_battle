from tkinter import *

l_con = [
    'Mob_size',
    'super_sec',
    'super_energy',
    'number_of_mobs',
    'on',
    'mob_lives',
    'touch',
    'shield',
    'Game_mode',
    'n',
    'Nuber_of_STRIKE',
    'kek'
]
spins = [1, 2, 3, 4, 6, 11]
checks = [5, 7, 8, 9, 10, 12]


class Settings:
    def __init__(self, l_con, spins, checks):
        self.labels = {}
        self.k = 0
        self.x = 0.1
        self.label = 'label'
        self.spinbox = 'spinbox'
        self.width = 0.2
        self.hieght = 0.1
        self.y = 0
        self.l_con = l_con
        self.checkbutton = 'checkbutton'
        self.spins = spins
        self.spinboxes = {}
        self.checks = checks
        self.checkbuttons = {}
        self.cvar = ''

        for i in self.spins:
            self.spinboxes.update({self.l_con[i - 1]: {}})
        for i in self.checks:
            self.checkbuttons.update({self.l_con[i - 1]: {}})
        for i in self.l_con:
            self.labels.update({i: {}})
        for i in self.labels:
            self.y = 0.1 + self.k / 20
            self.labels[i].update({
                self.label: {'x': self.x,
                             'width': self.width,
                             'hieght': self.hieght},
                self.spinbox: {},
                self.checkbutton: {}
            })
            self.labels[i][self.label].update({'y': self.y})
            print(self.labels[i])
            self.k = self.k + 1

        for t in self.spinboxes:
            self.labels[t].update({self.spinbox: {}})
            self.labels[t][self.spinbox].update({
                'y': self.labels[t][self.label]['y'],
                'x': self.labels[t][self.label]['x']
                     + self.width
            })
            print(self.labels[t])

        for t in self.checkbuttons:
            self.labels[t].update({self.checkbutton: {}})
            self.labels[t][self.checkbutton].update({
                'y': self.labels[t][self.label]['y'],
                'x': self.labels[t][self.label]['x']
                     + self.width,
                'cvar': self.cvar})
            print(self.labels[t])
        for i in self.l_con:
            l = self.labels[i][self.label]
            Label(text=i, bg='white').place(
                relx=l['x'],
                rely=l['y'],
                relwidth=l['width']
            )
            if self.labels[i][self.spinbox]:
                s = self.labels[i][self.spinbox]
                spin = Spinbox(
                    bg='yellow',
                    from_=1, to=20000
                ).place(
                    relx=s['x'],
                    rely=s['y'],
                    relwidth=0.2,
                    relheight=0.05
                )

            if self.labels[i][self.checkbutton]:
                self.c = self.labels[i][self.checkbutton]
                self.cvar = BooleanVar()
                self.cvar.set(0)
                Checkbutton(
                    bg='yellow',
                    variable=self.cvar,
                    onvalue=1,
                    offvalue=0).place(
                    relx=self.c['x'],
                    rely=self.c['y'],
                    relwidth=0.2,
                    relheight=0.05,
                )
                self.c.update({'cvar': self.cvar, 'cvar_meaning': self.cvar.get()})
        self.b = Button(text='Push', bg='red', command=push).place(
            relx=0.4,
            rely=0.8,
            relwidth=0.2,
            relheight=0.05
        )
        print(self.labels)


def push():
    d = open('Reference.txt', 'w')
    for i in menu.labels:
        p = menu.labels[i]
        if p['checkbutton']:
            p['checkbutton']['cvar_meaning'] = p['checkbutton']['cvar'].get()
        if p['checkbutton']:
            d.write(str(int(p['checkbutton']['cvar_meaning'])) + '\n')


root = Tk()
root.title("settings")
root.geometry('500x500')
menu = Settings(l_con, spins, checks)
root.mainloop()
print()