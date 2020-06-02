import tkinter as tk
from tkinter import ttk
from page import Page
from db import Database


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg='mint cream')
        label = tk.Label(self, text='Знайти пацієнта в базі',
                         font='Times 20', bg='mint cream')
        label.pack(side='top')

        # Name input
        self.patientName = tk.StringVar()
        inputFrame = tk.Frame(self, bg='mint cream')
        name = tk.Label(inputFrame, text='ПІБ: ',
                        font='Times 15', bg='mint cream')
        message_entry = ttk.Entry(
            inputFrame, textvariable=self.patientName, font='Times 15')

        # Search button
        s = ttk.Style()
        s.configure('my.TButton', font=('Times', 13))
        findButton = ttk.Button(
            inputFrame, text='  Пошук піцієнтів  ',
            style='my.TButton', command=self.fillList)

        # Names list
        listFrame = tk.Frame(self, bg='mint cream', )
        self.tree = ttk.Treeview(listFrame, height=90)
        self.tree['columns'] = ('one', 'two', 'three', 'four')
        self.tree.column('#0', width=270, minwidth=270, stretch=tk.NO)
        self.tree.column('one', width=145, minwidth=145, stretch=tk.NO)
        self.tree.column('two', width=0, minwidth=0, stretch=tk.NO)
        self.tree.column('three', width=0, minwidth=0, stretch=tk.NO)
        self.tree.column('four', width=0, minwidth=0, stretch=tk.NO)
        self.tree.heading('#0', text='Ім\'я', anchor=tk.W)
        self.tree.heading('one', text='Дата народження', anchor=tk.W)

        # Database stuff
        self.db = Database('patients.db')
        for patient in self.db.fetch():
            self.tree.insert('', 1, text=patient[1], values=(
                patient[2], patient[0], patient[3], patient[4]))

        # Patient data frame
        titles = ('ПІБ', 'Дата народження', 'Місце проживання', 'Стать')
        self.vars = (tk.StringVar(), tk.StringVar(),
                     tk.StringVar(), tk.StringVar(), tk.StringVar())
        dataInfo = tk.Frame(listFrame, pady=10, padx=10)
        dataInfo.pack(side='right', anchor='nw')
        self.dataFrame = tk.Frame(dataInfo, bg='azure3')
        self.dataFrame.pack(side='top', pady=10)
        for i in range(0, 4):
            tk.Label(self.dataFrame, text=str(titles[i]),
                     font='Times 13', bg='azure3').grid(
                         row=i, column=0, padx=10)
            tk.Label(self.dataFrame, textvariable=self.vars[i],
                     font='Times 13 italic', bg='azure3',
                     width=28).grid(row=i, column=1)
        ttk.Button(self.dataFrame, text='  Новий пацієнт  ',
                   style='my.TButton',
                   command=self.generateWindow).grid(row=6, column=0, pady=15)
        ttk.Button(self.dataFrame, text='  Продовжити  ',
                   style='my.TButton',
                   command=self.generateWindow).grid(row=6, column=1)

        # Pack widgets
        name.pack(side='left')
        message_entry.pack(side='left')
        inputFrame.pack(side='top', padx=20, anchor='nw')
        findButton.pack(side='left', padx=5)
        listFrame.pack(side='top', expand=1,
                       anchor='nw', padx=10, pady=10)
        self.tree.pack(side='left')

        self.tree.bind('<<TreeviewSelect>>', self.selected)

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
        print(self.vars[4].get())

    def generateWindow(self):
        window = tk.Toplevel()
        frame = tk.Frame(window, width='70', height='20')
        frame.pack(side='top', padx=10, pady=10, expand=1, anchor='nw')

        self.newPatientName = tk.StringVar()
        self.newPatientDate = tk.StringVar()
        self.newPatientPlace = tk.StringVar()
        tk.Label(frame, text="ПІБ: ").grid(row=0, column=0)
        ttk.Entry(frame, textvariable=self.newPatientName,
                  font='Times 14').grid(row=0, column=1)
        tk.Label(frame, text="Місце проживання: ").grid(row=1, column=0)
        ttk.Entry(frame, textvariable=self.newPatientDate,
                  font='Times 14').grid(row=1, column=1)
        tk.Label(frame, text="Дата народження: ").grid(row=2, column=0)
        ttk.Entry(frame, textvariable=self.newPatientPlace,
                  font='Times 14').grid(row=2, column=1)
        tk.Label(frame, text="Стать: ").grid(row=3, column=0)
        frameRad = tk.Frame(frame)
        frameRad.grid(row=3, column=1)

        self.myvar = tk.IntVar(frameRad)
        ttk.Radiobutton(frameRad, text='Чоловій', variable=self.myvar,
                        value=0).grid(row=0, column=0, padx=2, pady=1)
        ttk.Radiobutton(frameRad, text='Жінка', variable=self.myvar,
                        value=1).grid(row=0, column=1, padx=2, pady=1)
        frameBtn = tk.Frame(window, height='10')
        frameBtn.pack(side='bottom', padx=5, pady=2, expand=1, anchor='e')

        def cancelBtn():
            print(self.myvar.get())
            window.destroy()
            window.update()

        def acceptBtn():
            print(self.myvar.get())
            window.destroy()
            window.update()

        ttk.Button(frameBtn, text='  Продовжити  ',
                   style='my.TButton',
                   command=acceptBtn).pack(side='right')
        ttk.Button(frameBtn, text='  Відмінити  ',
                   style='my.TButton',
                   command=cancelBtn).pack(side='right')
