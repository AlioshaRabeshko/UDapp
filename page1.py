import tkinter as tk
from tkinter import ttk
from page import Page
from db import Database


class InputBox():
    def __init__(self, dbObj):
        self.db = dbObj
        self.window = tk.Toplevel()
        self.window.title('Добавити нового пацієнта')
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
        self.window.destroy()
        self.window.update()

    def acceptBtn(self):
        if (len(self.newPatientName.get()) != 0 and
            len(self.newPatientDate.get()) != 0 and
                len(self.newPatientPlace.get()) != 0):
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


class EditBox():
    def __init__(self, dbObj, data):
        self.db = dbObj
        self.data = data
        self.window = tk.Toplevel()
        self.window.title('Добавити нового пацієнта')
        self.frame = tk.Frame(self.window)
        self.frame.pack(side='top', padx=10, pady=10, expand=1, anchor='nw')

        self.showEntry()
        self.showRadBtn()

        frameBtn = tk.Frame(self.window, height='10')
        frameBtn.pack(side='bottom', padx=5, pady=2, expand=1, anchor='e')

        ttk.Button(frameBtn, text='  Зберегти  ',
                   style='my.TButton',
                   command=self.acceptBtn).pack(side='right')
        ttk.Button(frameBtn, text='  Видалити  ',
                   style='my.TButton',
                   command=self.deleteBtn).pack(side='right')
        ttk.Button(frameBtn, text='  Відмінити  ',
                   style='my.TButton',
                   command=self.cancelBtn).pack(side='right')

    def showEntry(self):
        self.patientName = self.data[0]
        self.patientDate = self.data[1]
        self.patientPlace = self.data[2]
        tk.Label(self.frame, text="ПІБ: ").grid(row=0, column=0)
        ttk.Entry(self.frame, textvariable=self.patientName,
                  font='Times 14', width='25').grid(row=0, column=1)
        tk.Label(self.frame, text="Місце проживання: ").grid(row=1, column=0)
        ttk.Entry(self.frame, textvariable=self.patientPlace,
                  font='Times 14', width='25').grid(row=1, column=1)
        tk.Label(self.frame, text="Дата народження: ").grid(row=2, column=0)
        ttk.Entry(self.frame, textvariable=self.patientDate,
                  font='Times 14', width='25').grid(row=2, column=1)
        tk.Label(self.frame, text="Стать: ").grid(row=3, column=0)

    def showRadBtn(self):
        self.frameRad = tk.Frame(self.frame)
        self.frameRad.grid(row=3, column=1)
        self.myvar = tk.IntVar(self.frameRad)
        if self.data[3].get() == 'Ч':
            self.myvar.set(0)
        elif self.data[3].get() == 'Ж':
            self.myvar.set(1)
        ttk.Radiobutton(self.frameRad, text='Чоловій', variable=self.myvar,
                        value=0).grid(row=0, column=0, padx=2, pady=1)
        ttk.Radiobutton(self.frameRad, text='Жінка', variable=self.myvar,
                        value=1).grid(row=0, column=1, padx=2, pady=1)

    def cancelBtn(self):
        self.window.destroy()
        self.window.update()

    def deleteBtn(self):
        self.db.delete(self.data[4].get())
        self.window.destroy()
        self.window.update()

    def acceptBtn(self):
        if (len(self.patientName.get()) != 0 and
            len(self.patientDate.get()) != 0 and
                len(self.patientPlace.get()) != 0):
            self.db.update(self.data[4].get(), {
                'name': self.patientName.get(),
                'birthday': self.patientDate.get(),
                'livingPlace': self.patientPlace.get(),
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

        self.buildLeftBar()
        self.loadList()
        self.printRightBar()

    def buildLeftBar(self):
        self.patientName = tk.StringVar()
        listFrame = tk.Frame(self, bg='mint cream', )

        inputFrame = tk.Frame(listFrame, bg='mint cream')
        inputFrame.pack(side='top', padx=5, pady=10, anchor='nw')
        tk.Label(inputFrame, text='ПІБ: ',
                 font='Times 15', bg='mint cream').pack(side='left')
        ttk.Entry(inputFrame, textvariable=self.patientName,
                  font='Times 15').pack(side='left')
        s = ttk.Style()
        s.configure('my.TButton', font=('Times', 13))
        ttk.Button(inputFrame, text='  Пошук піцієнтів  ',
                   style='my.TButton',
                   command=self.fillList).pack(side='left', padx=5)

        self.tree = ttk.Treeview(listFrame, height=90)
        self.tree['columns'] = ('one', 'two', 'three', 'four')
        self.tree.column('#0', width=270, minwidth=270, stretch=tk.NO)
        self.tree.column('one', width=145, minwidth=145, stretch=tk.NO)
        self.tree.column('two', width=0, minwidth=0, stretch=tk.NO)
        self.tree.column('three', width=0, minwidth=0, stretch=tk.NO)
        self.tree.column('four', width=0, minwidth=0, stretch=tk.NO)
        self.tree.heading('#0', text='Ім\'я', anchor=tk.W)
        self.tree.heading('one', text='Дата народження', anchor=tk.W)

        listFrame.pack(side='left', padx=10, pady=10)
        self.tree.pack(side='top')
        self.tree.bind('<<TreeviewSelect>>', self.selected)

    def printRightBar(self):
        titles = ('ПІБ', 'Дата народження', 'Місце проживання', 'Стать')
        self.vars = (tk.StringVar(), tk.StringVar(),
                     tk.StringVar(), tk.StringVar(), tk.StringVar())
        dataInfo = tk.Frame(self, pady=10, padx=10)
        dataInfo.pack(side='left', anchor='nw')
        dataFrame = tk.Frame(dataInfo, bg='azure3')
        dataFrame.pack(side='top', pady=10)
        for i in range(0, 4):
            tk.Label(dataFrame, text=str(titles[i]),
                     font='Times 13 bold', bg='azure3').grid(
                         row=i, column=0, padx=10)
            tk.Label(dataFrame, textvariable=self.vars[i],
                     font='Times 13 italic', bg='azure3',
                     width=28).grid(row=i, column=1)
        self.editBtn = ttk.Button(dataFrame, text='  Редагувати  ',
                                  style='my.TButton',
                                  command=self.generateEditWindow)
        self.editBtn.grid(row=6, column=0)
        self.editBtn.state(['disabled'])
        ttk.Button(dataFrame, text='  Новий пацієнт  ',
                   style='my.TButton',
                   command=self.generateIputWindow
                   ).grid(row=6, column=1, pady=15)

        titles = ({'name': 'Дослідження серця', 'template': 'tmp1', 'id': 'Id'},
                  {'name': '', 'template': '', 'id': ''})
        self.diags = (tk.StringVar(), tk.StringVar(),
                      tk.StringVar(), tk.StringVar(), tk.StringVar())
        self.treeDiag = ttk.Treeview(dataInfo, height=13)
        self.treeDiag['columns'] = ('one', 'two')
        self.treeDiag.column('#0', width=420, stretch='no')
        self.treeDiag.column('one', width=0, stretch='no')
        self.treeDiag.column('two', width=0, stretch='no')
        self.treeDiag.heading('#0', text='Тип обстеження', anchor='w')
        self.treeDiag.pack(side='top')
        for el in titles:
            self.treeDiag.insert('', 1, text=el['name'],
                                 values=(el['template'], el['id']))

        btn = tk.Frame(dataInfo, bg='azure3')
        btn.pack(side='top', pady=10)
        ttk.Button(btn, text='  Продовжити  ',
                   style='my.TButton',
                   command=self.switchPage).grid(row=6, column=1)

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
        self.editBtn.state(['!disabled'])
        self.vars[0].set(self.tree.item(self.tree.focus())['text'])
        self.vars[1].set(self.tree.item(self.tree.focus())['values'][0])
        self.vars[2].set(self.tree.item(self.tree.focus())['values'][2])
        self.vars[3].set(self.tree.item(self.tree.focus())['values'][3])
        self.vars[4].set(self.tree.item(self.tree.focus())['values'][1])

    def generateIputWindow(self):
        InputBox(self.db)

    def generateEditWindow(self):
        if len(self.vars[0].get()) == 0:
            return
        EditBox(self.db, self.vars)

    def setCb(self, pg):
        self.pg = pg

    def switchPage(self):
        self.pg.lift()
        self.pg.setInfo(self.vars, self.treeDiag.item(
            self.treeDiag.focus())['text'])
