import tkinter as tk
from tkinter import ttk
from page import Page
from db import Database


class DialogBox():
    def __init__(self, dbObj):
        self.db = dbObj
        self.window = tk.Toplevel()
        self.frame = tk.Frame(self.window)
        self.frame.pack(side='top', padx=10, pady=10, expand=1, anchor='nw')

        self.showEntry()
        self.showRadBtn()

        frameBtn = tk.Frame(self.window, height='10')
        frameBtn.pack(side='bottom', padx=5, pady=2, expand=1, anchor='e')

        ttk.Button(frameBtn, text='  Продовжити  ',
                   style='my.TButton',
                   command=self.acceptBtn).pack(side='right')
        ttk.Button(frameBtn, text='  Відмінити  ',
                   style='my.TButton',
                   command=self.cancelBtn).pack(side='right')

    def showEntry(self):
        self.newPatientName = tk.StringVar()
        self.newPatientDate = tk.StringVar()
        self.newPatientPlace = tk.StringVar()
        tk.Label(self.frame, text="ПІБ: ").grid(row=0, column=0)
        ttk.Entry(self.frame, textvariable=self.newPatientName,
                  font='Times 14', width='25').grid(row=0, column=1)
        tk.Label(self.frame, text="Місце проживання: ").grid(row=1, column=0)
        ttk.Entry(self.frame, textvariable=self.newPatientPlace,
                  font='Times 14', width='25').grid(row=1, column=1)
        tk.Label(self.frame, text="Дата народження: ").grid(row=2, column=0)
        ttk.Entry(self.frame, textvariable=self.newPatientDate,
                  font='Times 14', width='25').grid(row=2, column=1)
        tk.Label(self.frame, text="Стать: ").grid(row=3, column=0)

    def showRadBtn(self):
        self.frameRad = tk.Frame(self.frame)
        self.frameRad.grid(row=3, column=1)
        self.myvar = tk.IntVar(self.frameRad)
        ttk.Radiobutton(self.frameRad, text='Чоловій', variable=self.myvar,
                        value=0).grid(row=0, column=0, padx=2, pady=1)
        ttk.Radiobutton(self.frameRad, text='Жінка', variable=self.myvar,
                        value=1).grid(row=0, column=1, padx=2, pady=1)

    def cancelBtn(self):
        print(self.myvar.get())
        self.window.destroy()
        self.window.update()

    def acceptBtn(self):
        if (len(self.newPatientName.get()) != 0 and
            len(self.newPatientName.get()) != 0 and
                len(self.newPatientName.get()) != 0):
            self.db.insert({
                'name': self.newPatientName.get(),
                'birthday': self.newPatientDate.get(),
                'livingPlace': self.newPatientPlace.get(),
                'sex': self.getLetter()})
            self.window.destroy()
            self.window.update()

    def getLetter(self):
        if self.myvar.get() == 0:
            return 'Ч'
        return 'Ж'


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg='mint cream')
        label = tk.Label(self, text='Знайти пацієнта в базі',
                         font='Times 20', bg='mint cream')
        label.pack(side='top')

        self.db = Database('patients.db')

        self.searchField()
        self.buildList()
        self.loadList()
        self.printData()

    def searchField(self):
        self.patientName = tk.StringVar()
        inputFrame = tk.Frame(self, bg='mint cream')
        inputFrame.pack(side='top', padx=20, anchor='nw')
        tk.Label(inputFrame, text='ПІБ: ',
                 font='Times 15', bg='mint cream').pack(side='left')
        ttk.Entry(inputFrame, textvariable=self.patientName,
                  font='Times 15').pack(side='left')

        # Search button
        s = ttk.Style()
        s.configure('my.TButton', font=('Times', 13))
        ttk.Button(inputFrame, text='  Пошук піцієнтів  ',
                   style='my.TButton',
                   command=self.fillList).pack(side='left', padx=5)

    def buildList(self):
        self.listFrame = tk.Frame(self, bg='mint cream', )
        self.tree = ttk.Treeview(self.listFrame, height=90)
        self.tree['columns'] = ('one', 'two', 'three', 'four')
        self.tree.column('#0', width=270, minwidth=270, stretch=tk.NO)
        self.tree.column('one', width=145, minwidth=145, stretch=tk.NO)
        self.tree.column('two', width=0, minwidth=0, stretch=tk.NO)
        self.tree.column('three', width=0, minwidth=0, stretch=tk.NO)
        self.tree.column('four', width=0, minwidth=0, stretch=tk.NO)
        self.tree.heading('#0', text='Ім\'я', anchor=tk.W)
        self.tree.heading('one', text='Дата народження', anchor=tk.W)

        self.listFrame.pack(side='top', expand=1,
                            anchor='nw', padx=10, pady=10)
        self.tree.pack(side='left')
        self.tree.bind('<<TreeviewSelect>>', self.selected)

    def printData(self):
        titles = ('ПІБ', 'Дата народження', 'Місце проживання', 'Стать')
        self.vars = (tk.StringVar(), tk.StringVar(),
                     tk.StringVar(), tk.StringVar(), tk.StringVar())
        dataInfo = tk.Frame(self.listFrame, pady=10, padx=10)
        dataInfo.pack(side='right', anchor='nw')
        self.dataFrame = tk.Frame(dataInfo, bg='azure3')
        self.dataFrame.pack(side='top', pady=10)
        for i in range(0, 4):
            tk.Label(self.dataFrame, text=str(titles[i]),
                     font='Times 13 bold', bg='azure3').grid(
                         row=i, column=0, padx=10)
            tk.Label(self.dataFrame, textvariable=self.vars[i],
                     font='Times 13 italic', bg='azure3',
                     width=28).grid(row=i, column=1)
        ttk.Button(self.dataFrame, text='  Новий пацієнт  ',
                   style='my.TButton',
                   command=self.generateWindow).grid(row=6, column=0, pady=15)
        ttk.Button(self.dataFrame, text='  Вибрати тип обстеження  ',
                   style='my.TButton',
                   command=self.generateWindow).grid(row=6, column=1)

    def loadList(self):
        for patient in self.db.fetch():
            self.tree.insert('', 1, text=patient[1], values=(
                patient[2], patient[0], patient[3], patient[4]))

    def fillList(self):
        self.tree.delete(*self.tree.get_children())
        for patient in self.db.fetchByName(self.patientName.get()):
            self.tree.insert('', 1, text=patient[1], values=(
                patient[2], patient[0], patient[3], patient[4]))

    def selected(self, smth):
        self.vars[0].set(self.tree.item(self.tree.focus())['text'])
        self.vars[1].set(self.tree.item(self.tree.focus())['values'][0])
        self.vars[2].set(self.tree.item(self.tree.focus())['values'][2])
        self.vars[3].set(self.tree.item(self.tree.focus())['values'][3])
        self.vars[4].set(self.tree.item(self.tree.focus())['values'][1])

    def generateWindow(self):
        DialogBox(self.db)
