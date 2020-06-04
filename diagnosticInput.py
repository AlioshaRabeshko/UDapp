import tkinter as tk
from tkinter import ttk
from page import Page


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Сторінка 1', font='Times 11')
        label.pack(side='top')

        container1 = tk.Frame(self)
        container1.pack(side='top', anchor='nw')

        container1_1 = tk.Frame(container1, padx=5, pady=5, bg='azure3')
        container1_1.pack(side='left', anchor='nw', padx=7)
        self.var = [0]*24
        for i in range(24):
            self.var[i] = tk.StringVar()
        tk.Label(container1_1, font='Times 15', bg='azure3',
                 text='Порожнина').grid(row=0, column=2)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text=' ВТЛШ ').grid(row=1, column=0)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[0],
                  width=8).grid(row=1, column=1)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='КДР').grid(row=2, column=0)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[1],
                  width=8).grid(row=2, column=1)
        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text=' см').grid(row=2, column=2)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='КСР').grid(row=3, column=0)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[2],
                  width=8).grid(row=3, column=1)
        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text=' см').grid(row=3, column=2)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='КДО').grid(row=4, column=0)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[3],
                  width=8).grid(row=4, column=1)
        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text=' мл').grid(row=4, column=2)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='КСО').grid(row=5, column=0)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[4],
                  width=8).grid(row=5, column=1)
        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text=' мл').grid(row=5, column=2)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='УО').grid(row=1, column=3)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[5],
                  width=8).grid(row=1, column=4)
        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='мл ').grid(row=1, column=5)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='ФВ').grid(row=2, column=3)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[6],
                  width=8).grid(row=2, column=4)
        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='%').grid(row=2, column=5)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='ЧСС').grid(row=3, column=3)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[7],
                  width=8).grid(row=3, column=4)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='FS').grid(row=4, column=3)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[8],
                  width=8).grid(row=4, column=4)

        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='Маса \nміокарду ').grid(row=5, column=3)
        ttk.Entry(container1_1, font='Times 12', textvariable=self.var[9],
                  width=8).grid(row=5, column=4)
        tk.Label(container1_1, font='Times 12', bg='azure3',
                 text='см  ').grid(row=5, column=5)

        container1_2 = tk.Frame(container1, padx=15, pady=5, bg='azure3')
        container1_2.pack(side='left', expand=1, anchor='nw')
        tk.Label(container1_2, font='Times 15', bg='azure3',
                 text='Стінки').grid(row=0, column=1)

        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='ТМШП').grid(row=1, column=0)
        ttk.Entry(container1_2, font='Times 12', textvariable=self.var[10],
                  width=8).grid(row=1, column=1)
        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='см').grid(row=1, column=2)

        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='Кінез').grid(row=2, column=0)
        ttk.Entry(container1_2, font='Times 12', textvariable=self.var[11],
                  width=8).grid(row=2, column=1)

        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='ТЗС').grid(row=3, column=0)
        ttk.Entry(container1_2, font='Times 12', textvariable=self.var[12],
                  width=8).grid(row=3, column=1)
        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='см').grid(row=3, column=2)

        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='Кінез').grid(row=4, column=0)
        ttk.Entry(container1_2, font='Times 12', textvariable=self.var[13],
                  width=8).grid(row=4, column=1)
        tk.Label(container1_2, font='Times 9', bg='azure3',
                 text='').grid(row=5, column=0)

        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='      Наявність перикардіального випоту'
                 ).grid(row=0, column=3, columnspan=5)
        ttk.Entry(container1_2, font='Times 12', textvariable=self.var[14],
                  width=12).grid(row=1, column=3)
        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='см').grid(row=1, column=4)

        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='Діастолічна дисфункція'
                 ).grid(row=2, column=3, columnspan=3)
        ttk.Entry(container1_2, font='Times 12', textvariable=self.var[15],
                  width=12).grid(row=3, column=3)

        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='    Атипова хорда', anchor='w'
                 ).grid(row=4, column=3, columnspan=1)
        ttk.Entry(container1_2, font='Times 12', textvariable=self.var[16],
                  width=12).grid(row=5, column=3)
        tk.Label(container1_2, font='Times 12', bg='azure3',
                 text='см').grid(row=5, column=4)
        tk.Label(container1_2, font='Times 9', bg='azure3',
                 text='').grid(row=6)

        container2 = tk.Frame(self, padx=9, pady=5)
        container2.pack(side='top', anchor='nw')

        container2_1 = tk.Frame(container2, padx=15, pady=5, bg='azure3')
        container2_1.pack(side='left', padx=5)

        tk.Label(container2_1, font='Times 15', bg='azure3',
                 text='Мітральний клапан').grid(row=0, column=0)
        valC2_1 = ['Норма', 'Паралельний рух', 'П-подібний рух',
                   'Помірний фіброз', 'Виражений фіброз', 'Різкий фіброз',
                   'Кальциноз', 'Вегетації', 'Пролапс', 'Зворотній потік']
        self.comboboxC2_1 = ttk.Combobox(container2_1, values=valC2_1)
        self.comboboxC2_1.grid(row=1, column=0)

        container2_2 = tk.Frame(container2, padx=15, pady=5, bg='azure3')
        container2_2.pack(side='left', padx=7)

        tk.Label(container2_2, font='Times 15', bg='azure3',
                 text='Правий шлуночок').grid(row=0, column=0)
        valC2_2 = ['Нормальна порожнина', 'Збільшена порожнина',
                   'Нормальна стінка', 'Гіпертрофія', 'Скоротливість']
        self.comboboxC2_2 = ttk.Combobox(container2_2, values=valC2_2)
        self.comboboxC2_2.grid(row=1, column=0)

        container2_3 = tk.Frame(container2, padx=15, pady=5, bg='azure3')
        container2_3.pack(side='left', padx=5)

        tk.Label(container2_3, font='Times 15', bg='azure3',
                 text='Трикуспідальний клапан'
                 ).grid(row=0, column=0, columnspan=3)
        valC2_3 = ['Норма', 'Фіброз', 'Зворотній потік', 'Градієн регуляції']
        self.comboboxC2_3 = ttk.Combobox(container2_3, values=valC2_3)
        self.comboboxC2_3.grid(row=1, column=0)
        ttk.Entry(container2_3, font='Times 11', textvariable=self.var[17],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container2_3, font='Times 11', bg='azure3',
                 text='mmHg').grid(row=1, column=3)

        container3 = tk.Frame(self, padx=9)
        container3.pack(side='top')

        container3_1 = tk.Frame(container3, padx=15, pady=5, bg='azure3')
        container3_1.pack(side='left', padx=5)

        tk.Label(container3_1, font='Times 15', bg='azure3',
                 text='Ліве передсердя').grid(row=0, column=0, columnspan=3)
        valC3_1 = ['Норма', 'Помірно збільшене', 'Різко збільшене']
        self.comboboxC2 = ttk.Combobox(
            container3_1, values=valC3_1).grid(row=1, column=0)
        ttk.Entry(container3_1, font='Times 11', textvariable=self.var[18],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container3_1, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container3_2 = tk.Frame(container3, padx=15, pady=5, bg='azure3')
        container3_2.pack(side='left', padx=7)

        tk.Label(container3_2, font='Times 15', bg='azure3',
                 text='Праве передсердя').grid(row=0, column=0, columnspan=3)
        valC3_2 = ['Норма', 'Помірно збільшене', 'Різко збільшене']
        self.comboboxC2 = ttk.Combobox(
            container3_2, values=valC3_2).grid(row=1, column=0)
        ttk.Entry(container3_2, font='Times 11', textvariable=self.var[19],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container3_2, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container4 = tk.Frame(self, padx=9)
        container4.pack(side='top')

        container4_1 = tk.Frame(container4, padx=15, pady=5, bg='azure3')
        container4_1.pack(side='left', padx=5, pady=10)

        tk.Label(container4_1, font='Times 15', bg='azure3',
                 text='Аорта, аортальний клапан').grid(row=0, column=0, columnspan=3)
        valC4_1 = ['Норма', 'Помірний фіброз', 'Виражений фіброз',
                   'Різкий фіброз', 'Кальциноз', 'Вегетації',
                   'Систологічне розкриття', 'Діаметер аорти',
                   'Зворотній потік', 'Швидкість кровотоку', 'Градієнт тиску']
        self.comboboxC2 = ttk.Combobox(
            container4_1, values=valC4_1).grid(row=1, column=0)
        ttk.Entry(container4_1, font='Times 11', textvariable=self.var[19],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container4_1, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container4_2 = tk.Frame(container4, padx=15, pady=5, bg='azure3')
        container4_2.pack(side='left', padx=7)

        tk.Label(container4_2, font='Times 15', bg='azure3',
                 text='Клапан легенвої артерії').grid(row=0, column=0, columnspan=3)
        valC4_2 = ['Норма', 'Фіброз', 'Не локується', 'Гіпертензія',
                   'Регургітація', 'V-кровотоку', 'Градієнт тиску']
        self.comboboxC2 = ttk.Combobox(
            container4_2, values=valC4_2).grid(row=1, column=0)
        ttk.Entry(container4_2, font='Times 11', textvariable=self.var[19],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container4_2, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container5 = tk.Frame(self, padx=9)
        container5.pack(side='top')

        self.textArea = tk.Text(
            container5, font='Times 11', padx=3, width=120, height=5)
        self.textArea.pack()


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Сторінка 2', bg='mint cream')
        label.pack(side='top')


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Сторінка 3', bg='mint cream')
        label.pack(side='top')


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Сторінка 4', bg='mint cream')
        label.pack(side='top')


class DiagnosticInput(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(
            self, text=' Ввід даних про обстеження ',
            font='Times 15', bg='mint cream')
        label.pack(side='top')

        self.config(bg='mint cream', padx=5, pady=5)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        container = tk.Frame(self, bg='mint cream')
        container.pack(side='top', fill='both', expand=True)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        p1.show()
