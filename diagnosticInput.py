import tkinter as tk
from tkinter import ttk
from page import Page
from docxtpl import DocxTemplate
from datetime import date
import io, os, sys, config


# class FormConstructor:
    # def __init__(self, diagName):


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Сторінка 1', font='Times 11')
        label.pack(side='top')
        container1 = tk.Frame(self)
        container1.pack(side='top')

        container1_1 = tk.Frame(container1, padx=5, pady=5, bg='azure3')
        container1_1.pack(side='left', padx=7)
        self.var = [0]*24
        for i in range(24):
            self.var[i] = tk.StringVar()
        tk.Label(container1_1, font='Times 15', bg='azure3',
                 text='Порожнина').grid(row=0, column=2, columnspan=2)

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
                 text=' мл').grid(row=5, column=0)
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
        container2.pack(side='top')

        container2_1 = tk.Frame(container2, padx=15, pady=5, bg='azure3')
        container2_1.pack(side='left', padx=5)

        tk.Label(container2_1, font='Times 15', bg='azure3',
                 text='Мітральний клапан').grid(row=0, column=0)
        valC2_1 = ['Норма', 'Паралельний рух', 'П-подібний рух',
                   'Помірний фіброз', 'Виражений фіброз', 'Різкий фіброз',
                   'Кальциноз', 'Вегетації', 'Пролапс', 'Зворотній потік']
        self.combobox2_1 = ttk.Combobox(container2_1, values=valC2_1)
        self.combobox2_1.grid(row=1, column=0)

        container2_2 = tk.Frame(container2, padx=15, pady=5, bg='azure3')
        container2_2.pack(side='left', padx=7)

        tk.Label(container2_2, font='Times 15', bg='azure3',
                 text='Правий шлуночок').grid(row=0, column=0)
        valC2_2 = ['Нормальна порожнина', 'Збільшена порожнина',
                   'Нормальна стінка', 'Гіпертрофія', 'Скоротливість']
        self.combobox2_2 = ttk.Combobox(container2_2, values=valC2_2)
        self.combobox2_2.grid(row=1, column=0)

        container2_3 = tk.Frame(container2, padx=15, pady=5, bg='azure3')
        container2_3.pack(side='left', padx=5)

        tk.Label(container2_3, font='Times 15', bg='azure3',
                 text='Трикуспідальний клапан'
                 ).grid(row=0, column=0, columnspan=3)
        valC2_3 = ['Норма', 'Фіброз', 'Зворотній потік', 'Градієн регуляції']
        self.combobox2_3 = ttk.Combobox(container2_3, values=valC2_3)
        self.combobox2_3.grid(row=1, column=0)
        def selectedItem23(smth):
            if self.combobox2_3.get() == 'Градієн регуляції':
                self.ent1.grid(row=1, column=2, padx=6)
                self.lab1.grid(row=1, column=3)
            else:
                self.ent1.grid_forget()
                self.lab1.grid_forget()

        self.combobox2_3.bind('<<ComboboxSelected>>', selectedItem23)
        self.ent1 = ttk.Entry(container2_3, font='Times 11', textvariable=self.var[17],
                  width=12)
        self.lab1 = tk.Label(container2_3, font='Times 11', bg='azure3', text='mmHg')

        container3 = tk.Frame(self, padx=9)
        container3.pack(side='top')

        container3_1 = tk.Frame(container3, padx=15, pady=5, bg='azure3')
        container3_1.pack(side='left', padx=5)

        tk.Label(container3_1, font='Times 15', bg='azure3',
                 text='Ліве передсердя').grid(row=0, column=0, columnspan=3)
        valC3_1 = ['Норма', 'Помірно збільшене', 'Різко збільшене']
        self.combobox3_1 = ttk.Combobox(container3_1, values=valC3_1)
        self.combobox3_1.grid(row=1, column=0)
        ttk.Entry(container3_1, font='Times 11', textvariable=self.var[18],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container3_1, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container3_2 = tk.Frame(container3, padx=15, pady=5, bg='azure3')
        container3_2.pack(side='left', padx=7)

        tk.Label(container3_2, font='Times 15', bg='azure3',
                 text='Праве передсердя').grid(row=0, column=0, columnspan=3)
        valC3_2 = ['Норма', 'Помірно збільшене', 'Різко збільшене']
        self.combobox3_2 = ttk.Combobox(container3_2, values=valC3_2)
        self.combobox3_2.grid(row=1, column=0)
        ttk.Entry(container3_1, font='Times 11', textvariable=self.var[19],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container3_1, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container4 = tk.Frame(self, padx=9)
        container4.pack(side='top')

        container4_1 = tk.Frame(container4, padx=15, pady=5, bg='azure3')
        container4_1.pack(side='left', padx=5, pady=10)

        tk.Label(container4_1, font='Times 15', bg='azure3',
                 text='Аорта, аортальний клапан'
                 ).grid(row=0, column=0, columnspan=3)
        valC4_1 = ['Норма', 'Помірний фіброз', 'Виражений фіброз',
                   'Різкий фіброз', 'Кальциноз', 'Вегетації',
                   'Систологічне розкриття', 'Діаметер аорти',
                   'Зворотній потік', 'Швидкість кровотоку', 'Градієнт тиску']
        self.combobox4_1 = ttk.Combobox(container4_1, values=valC4_1)
        self.combobox4_1.grid(row=1, column=0)
        ttk.Entry(container4_1, font='Times 11', textvariable=self.var[19],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container4_1, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container4_2 = tk.Frame(container4, padx=15, pady=5, bg='azure3')
        container4_2.pack(side='left', padx=7)

        tk.Label(container4_2, font='Times 15', bg='azure3',
                 text='Клапан легенвої артерії'
                 ).grid(row=0, column=0, columnspan=3)
        valC4_2 = ['Норма', 'Фіброз', 'Не локується', 'Гіпертензія',
                   'Регургітація', 'V-кровотоку', 'Градієнт тиску']
        self.combobox4_2 = ttk.Combobox(container4_2, values=valC4_2)
        self.combobox4_2.grid(row=1, column=0)
        ttk.Entry(container4_2, font='Times 11', textvariable=self.var[19],
                  width=12).grid(row=1, column=2, padx=6)
        tk.Label(container4_2, font='Times 11', bg='azure3',
                 text='см').grid(row=1, column=3)

        container5 = tk.Frame(self, padx=9)
        container5.pack(side='top')

        self.textArea = tk.Text(
            container5, font='Times 11', padx=3, width=120, height=5)
        self.textArea.grid(row=0, column=0, columnspan=8)

        ttk.Button(container5, text='  Продовжити  ', command=self.continueBtn,
                   style='my.TButton').grid(row=1, column=7)

    def continueBtn(self):
        doc = DocxTemplate('tmps/tmp.docx')
        context = {
            'diagnosticsName': self.diagData,
            'name': self.patientData[0].get(),
            'date': self.patientData[1].get(),
            'vtlsh': self.var[0].get(),
            'kdr': self.var[1].get(),
            'kcp': self.var[2].get(),
            'kdo': self.var[3].get(),
            'kso': self.var[4].get(),
            'uo': self.var[5].get(),
            'fv': self.var[6].get(),
            'chss': self.var[7].get(),
            'fs': self.var[8].get(),
            'mw': self.var[9].get(),
            'tmshp': self.var[10].get(),
            'kin1': self.var[11].get(),
            'tzs': self.var[12].get(),
            'kin2': self.var[13].get(),
            'pv': self.var[14].get(),
            'dd': self.var[15].get(),
            'ah': self.var[16].get(),
            'mk': self.combobox2_1.get(),
            'psh': self.combobox2_2.get(),
            'tkk': self.combobox2_3.get(),
            'lp': self.combobox3_1.get(),
            'pp': self.combobox3_2.get(),
            'aort': self.combobox4_1.get(),
            'kla': self.combobox4_2.get(),
            'zakl': self.textArea.get(1.0, tk.END),
            'dn': 'Ім\'я лікаря'
        }
        doc.render(context)
        doc.save('final.docx')
        try:
            os.system('libreoffice6.4 ' + './final.docx')
            os.system('start ' + './final.docx')
        except err:
            print(err)

    def setInfo(self, patientData, diagData):
        self.patientData = patientData
        self.diagData = diagData


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Обстеження органів черевної порожнини з кольоровим картуванням', font='Times 11')
        label.pack(side='top')
        
        self.var = [None]*29
        for i in range(29):
            self.var[i] = tk.StringVar()

        container1 = tk.Frame(self)
        container1.pack(side='top')
        tk.Label(container1, text='Печінка', font='Times 13 bold', bg='azure3').pack(side='top', fill='x')

        container1_1 = tk.Frame(container1, pady=1)
        container1_1.pack(side='top', fill='x')
        container1_1_0 = tk.Frame(container1_1, padx=2, bg='azure3')
        container1_1_0.pack(side='left', fill='both')
        tk.Label(container1_1_0, text='Розміри', font='Times 12', bg='azure3').pack(side='top')
        container1_1_0_1 = tk.Frame(container1_1_0, pady=2, bg='azure3')
        container1_1_0_1.pack(side='top', pady=2, fill='both')
        tk.Label(container1_1_0_1, text='Ліва доля:    ', font='Times 12', bg='azure3').pack(side='left')
        ttk.Entry(container1_1_0_1, font='Times 12', textvariable=self.var[0], width=8).pack(side='left')
        tk.Label(container1_1_0_1, text=' мм', font='Times 12', bg='azure3').pack(side='left')

        container1_1_0_2 = tk.Frame(container1_1_0, pady=2, bg='azure3')
        container1_1_0_2.pack(side='top', pady=2, fill='both')
        tk.Label(container1_1_0_2, text='Права доля: ', font='Times 12', bg='azure3').pack(side='left')
        ttk.Entry(container1_1_0_2, font='Times 12', textvariable=self.var[1], width=8).pack(side='left')
        tk.Label(container1_1_0_2, text=' мм', font='Times 12', bg='azure3').pack(side='left')

        container1_1_1 = tk.Frame(container1_1, padx=5, bg='azure3')
        container1_1_1.pack(side='left', padx=1, fill='both')
        tk.Label(container1_1_1, text='Контури', font='Times 12', bg='azure3').pack(side='top')
        container1_1_1_1 = tk.Frame(container1_1_1, pady=5, bg='azure3')
        container1_1_1_1.pack(side='top', pady=2, fill='both')
        ttk.Radiobutton(container1_1_1_1, text='Чіткі', variable=self.var[2], value='Чіткі').grid(row=0, column=0, padx=5, pady=1)
        ttk.Radiobutton(container1_1_1_1, text='Нечіткі', variable=self.var[2], value='Нечіткі').grid(row=0, column=1, padx=5, pady=1)
        ttk.Radiobutton(container1_1_1_1, text='Рівні', variable=self.var[3], value=' рівні').grid(row=1, column=0, padx=5, pady=1)
        ttk.Radiobutton(container1_1_1_1, text='Нерівні', variable=self.var[3], value=' нерівні').grid(row=1, column=1, padx=5, pady=1)
        
        container1_1_2 = tk.Frame(container1_1, pady=2, bg='azure3')
        container1_1_2.pack(side='left', fill='both')
        tk.Label(container1_1_2, text='Краї', font='Times 12', bg='azure3').pack(side='top')
        ttk.Radiobutton(container1_1_2, text='Гострі', variable=self.var[4], value='Гострі').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container1_1_2, text='Заокруглені', variable=self.var[4], value='Заокруглені').pack(side='top', padx=10, pady=1)

        container1_1_3 = tk.Frame(container1_1, pady=2, bg='azure3')
        container1_1_3.pack(side='left', padx=1, fill='both')
        tk.Label(container1_1_3, text='Ехоструктура', font='Times 12', bg='azure3').pack(side='top')
        ttk.Radiobutton(container1_1_3, text='Дрібнозерниста', variable=self.var[5], value='Дрібнозерниста').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container1_1_3, text='Однорідна', variable=self.var[5], value='Однорідна').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container1_1_3, text='Неоднорідна', variable=self.var[5], value='Неоднорідна').pack(side='top', padx=10, pady=1)

        container1_1_4 = tk.Frame(container1_1, pady=2, bg='azure3')
        container1_1_4.pack(side='left', fill='both')
        tk.Label(container1_1_4, text='Ехогенність', font='Times 12', bg='azure3').pack(side='top')
        ttk.Radiobutton(container1_1_4, text='Підвищена', variable=self.var[6], value='Підвищена').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container1_1_4, text='Знижена', variable=self.var[6], value='Знижена').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container1_1_4, text='Без змін', variable=self.var[6], value='Без змін').pack(side='top', padx=10, pady=1)

        container1_1_5 = tk.Frame(container1_1, pady=2, bg='azure3')
        container1_1_5.pack(side='left', fill='both', padx=1)
        container1_1_5_1 = tk.Frame(container1_1_5, pady=4, padx=4, bg='azure3')
        container1_1_5_1.pack(side='top', fill='both')
        tk.Label(container1_1_5_1, text='Ворітна вежа: ', font='Times 12', bg='azure3').pack(side='left')
        ttk.Entry(container1_1_5_1, font='Times 12', textvariable=self.var[7], width=4).pack(side='left')
        tk.Label(container1_1_5_1, text=' мм', font='Times 12', bg='azure3').pack(side='left')
        container1_1_5_2 = tk.Frame(container1_1_5, pady=4, padx=4, bg='azure3')
        container1_1_5_2.pack(side='top', fill='both')
        tk.Label(container1_1_5_2, text='НПВ:               ', font='Times 12', bg='azure3').pack(side='left')
        ttk.Entry(container1_1_5_2, font='Times 12', textvariable=self.var[8], width=4).pack(side='left', padx=1)
        tk.Label(container1_1_5_2, text=' мм', font='Times 12', bg='azure3').pack(side='left')
        container1_1_5_2 = tk.Frame(container1_1_5, pady=4, padx=4, bg='azure3')
        container1_1_5_2.pack(side='top', fill='both')
        tk.Label(container1_1_5_2, text='Холедох:         ', font='Times 12', bg='azure3').pack(side='left')
        ttk.Entry(container1_1_5_2, font='Times 12', textvariable=self.var[9], width=4).pack(side='left')
        tk.Label(container1_1_5_2, text=' мм', font='Times 12', bg='azure3').pack(side='left')

        container2 = tk.Frame(self)
        container2.pack(side='top', pady=2)
        
        container2_2 = tk.Frame(container2, pady=1)
        container2_2.pack(side='top', fill='x')
        tk.Label(container2_2, text='Жовчний міхур', font='Times 13 bold', bg='azure3', padx=10).pack(side='left', fill='both')
        container2_2_1 = tk.Frame(container2_2, pady=2, bg='azure3')
        container2_2_1.pack(side='left', fill='both', padx=1)
        ttk.Radiobutton(container2_2_1, text='Визначається', variable=self.var[10], value='Визначається').pack(side='top', padx=15, pady=1)
        ttk.Radiobutton(container2_2_1, text='Не визначається', variable=self.var[10], value='Не визначається').pack(side='top', padx=15, pady=1)

        container2_2_2 = tk.Frame(container2_2, padx=2, bg='azure3')
        container2_2_2.pack(side='left', fill='both')
        container2_2_2_1 = tk.Frame(container2_2_2, pady=2, bg='azure3')
        container2_2_2_1.pack(side='top', pady=2, fill='both')
        tk.Label(container2_2_2_1, text='Розміри: ', font='Times 12', bg='azure3').pack(side='left')
        ttk.Entry(container2_2_2_1, font='Times 12', textvariable=self.var[11], width=8).pack(side='left', padx=1)
        tk.Label(container2_2_2_1, text=' мм', font='Times 12', bg='azure3').pack(side='left')
        container2_2_2_2 = tk.Frame(container2_2_2, pady=2, bg='azure3')
        container2_2_2_2.pack(side='top', pady=2, fill='both')
        tk.Label(container2_2_2_2, text='Стінки:   ', font='Times 12', bg='azure3').pack(side='left')
        ttk.Entry(container2_2_2_2, font='Times 12', textvariable=self.var[12], width=8).pack(side='left')
        tk.Label(container2_2_2_2, text=' мм', font='Times 12', bg='azure3').pack(side='left')

        
        container2_2_3 = tk.Frame(container2_2, padx=2, bg='azure3')
        container2_2_3.pack(side='left', fill='both', padx=1)
        container2_2_3_1 = tk.Frame(container2_2_3, padx=5, pady=5, bg='azure3')
        container2_2_3_1.pack(side='top', pady=2, fill='both')
        ttk.Radiobutton(container2_2_3_1, text='Чіткі', variable=self.var[13], value='Чіткі').grid(row=0, column=0, padx=5, pady=1)
        ttk.Radiobutton(container2_2_3_1, text='Нечіткі', variable=self.var[13], value='Нечіткі').grid(row=0, column=1, padx=5, pady=1)
        ttk.Radiobutton(container2_2_3_1, text='Рівні', variable=self.var[14], value=' рівні').grid(row=1, column=0, padx=5, pady=1)
        ttk.Radiobutton(container2_2_3_1, text='Нерівні', variable=self.var[14], value=' нерівні').grid(row=1, column=1, padx=5, pady=1)


        container3 = tk.Frame(self)
        container3.pack(side='top')
        tk.Label(container3, text='Підшлункова залоза', font='Times 13 bold', bg='azure3').pack(side='top', fill='x')

        container3_2 = tk.Frame(container3, pady=1)
        container3_2.pack(side='top', fill='x')
        
        container3_2_1 = tk.Frame(container3_2, padx=2, bg='azure3')
        container3_2_1.pack(side='left', fill='both')
        container3_2_1_1 = tk.Frame(container3_2_1, padx=5, pady=5, bg='azure3')
        container3_2_1_1.pack(side='top', pady=2, fill='both')
        ttk.Radiobutton(container3_2_1_1, text='Візуалізується', variable=self.var[15], value='Візуалізується').grid(row=0, column=0, padx=5, pady=1)
        ttk.Radiobutton(container3_2_1_1, text='Не візуалізується', variable=self.var[15], value='Не візуалізується').grid(row=0, column=1, padx=5, pady=1)
        ttk.Radiobutton(container3_2_1_1, text='Повністю         ', variable=self.var[16], value=' повністю').grid(row=1, column=0, padx=5, pady=1)
        ttk.Radiobutton(container3_2_1_1, text='Неповністю          ', variable=self.var[16], value=' неповністю').grid(row=1, column=1, padx=5, pady=1)

        container3_2_2 = tk.Frame(container3_2, padx=2, bg='azure3')
        container3_2_2.pack(side='left', fill='both', padx=1)
        container3_2_2_1 = tk.Frame(container3_2_2, padx=5, pady=5, bg='azure3')
        container3_2_2_1.pack(side='top', pady=2, fill='both')
        tk.Label(container3_2_2_1, text='Розміри: ', font='Times 12', bg='azure3').pack(side='left', fill='x')
        ttk.Entry(container3_2_2_1, font='Times 12', textvariable=self.var[17], width=4).pack(side='left', padx=1)
        ttk.Entry(container3_2_2_1, font='Times 12', textvariable=self.var[18], width=4).pack(side='left', padx=1)
        ttk.Entry(container3_2_2_1, font='Times 12', textvariable=self.var[19], width=4).pack(side='left', padx=1)
        tk.Label(container3_2_2_1, text=' мм', font='Times 12', bg='azure3').pack(side='left', fill='x')
        container3_2_2_2 = tk.Frame(container3_2_2, padx=5, pady=5, bg='azure3')
        container3_2_2_2.pack(side='top', pady=2, fill='both')
        tk.Label(container3_2_2_2, text='Структура: ', font='Times 12', bg='azure3').pack(side='left', fill='x')
        ttk.Radiobutton(container3_2_2_2, text='Однорідна', variable=self.var[20], value='Однорідна').pack(side='left', padx=2, pady=1)
        ttk.Radiobutton(container3_2_2_2, text='Неднорідна', variable=self.var[20], value='Неднорідна').pack(side='left', pady=1)

        container3_2_3 = tk.Frame(container3_2, padx=2, bg='azure3')
        container3_2_3.pack(side='left', fill='both')
        tk.Label(container3_2_3, text='Ехогенність', font='Times 12', bg='azure3').pack(side='top', fill='x')
        ttk.Radiobutton(container3_2_3, text='Підвищена', variable=self.var[21], value='Підвищена').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container3_2_3, text='Знижена', variable=self.var[21], value='Знижена').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container3_2_3, text='Без змін', variable=self.var[21], value='Без змін').pack(side='top', padx=10, pady=1)

        container3_2_3 = tk.Frame(container3_2, padx=2, bg='azure3')
        container3_2_3.pack(side='left', fill='both', padx=1)
        tk.Label(container3_2_3, text='Панкреатична протока', font='Times 12', bg='azure3').pack(side='top', fill='x')
        container3_2_3_1 = tk.Frame(container3_2_3, padx=5, pady=5, bg='azure3')
        container3_2_3_1.pack(side='top', pady=2, fill='both')
        ttk.Entry(container3_2_3_1, font='Times 12', textvariable=self.var[22], width=8).pack(side='left', padx=1)
        tk.Label(container3_2_3_1, text=' мм', font='Times 12', bg='azure3').pack(side='left', fill='x')
        
        
        container4 = tk.Frame(self)
        container4.pack(side='top', pady=2)

        container4_1 = tk.Frame(container4, pady=1)
        container4_1.pack(side='top', fill='x')
        tk.Label(container4_1, text='Селезінка', font='Times 13 bold', bg='azure3', padx=10).pack(side='left', fill='both')
        
        container4_1_1 = tk.Frame(container4_1, padx=2, bg='azure3')
        container4_1_1.pack(side='left', fill='both', padx=1)
        tk.Label(container4_1_1, text='Розміри', font='Times 12', bg='azure3').pack(side='top', fill='x')
        container4_1_1_1 = tk.Frame(container4_1_1, padx=5, pady=5, bg='azure3')
        container4_1_1_1.pack(side='top', pady=2, fill='both')
        ttk.Entry(container4_1_1_1, font='Times 12', textvariable=self.var[23], width=8).pack(side='left', padx=1)
        tk.Label(container4_1_1_1, text=' мм', font='Times 12', bg='azure3').pack(side='left', fill='x')

        container4_1_2 = tk.Frame(container4_1, padx=2, bg='azure3')
        container4_1_2.pack(side='left', fill='both')
        tk.Label(container4_1_2, text='Контури', font='Times 12', bg='azure3').pack(side='top', fill='x')
        container4_1_2_1 = tk.Frame(container4_1_2, padx=5, pady=5, bg='azure3')
        container4_1_2_1.pack(side='top', pady=2, fill='both')
        ttk.Radiobutton(container4_1_2_1, text='Чіткі', variable=self.var[24], value='Чіткі').grid(row=0, column=0, padx=5, pady=1)
        ttk.Radiobutton(container4_1_2_1, text='Нечіткі', variable=self.var[24], value='Нечіткі').grid(row=0, column=1, padx=5, pady=1)
        ttk.Radiobutton(container4_1_2_1, text='Рівні', variable=self.var[25], value=' рівні').grid(row=1, column=0, padx=5, pady=1)
        ttk.Radiobutton(container4_1_2_1, text='Нерівні', variable=self.var[25], value=' нерівні').grid(row=1, column=1, padx=5, pady=1)

        container4_1_3 = tk.Frame(container4_1, pady=2, bg='azure3')
        container4_1_3.pack(side='left', padx=1, fill='both')
        tk.Label(container4_1_3, text='Ехоструктура', font='Times 12', bg='azure3').pack(side='top')
        ttk.Radiobutton(container4_1_3, text='Дрібнозерниста', variable=self.var[26], value='Дрібнозерниста').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container4_1_3, text='Однорідна', variable=self.var[26], value='Однорідна').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container4_1_3, text='Неоднорідна', variable=self.var[26], value='Неоднорідна').pack(side='top', padx=10, pady=1)

        container4_1_4 = tk.Frame(container4_1, pady=2, bg='azure3')
        container4_1_4.pack(side='left', fill='both')
        tk.Label(container4_1_4, text='Ехогенність', font='Times 12', bg='azure3').pack(side='top')
        ttk.Radiobutton(container4_1_4, text='Підвищена', variable=self.var[27], value='Підвищена').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container4_1_4, text='Знижена', variable=self.var[27], value='Знижена').pack(side='top', padx=10, pady=1)
        ttk.Radiobutton(container4_1_4, text='Без змін', variable=self.var[27], value='Без змін').pack(side='top', padx=10, pady=1)

        container4_1_5 = tk.Frame(container4_1, padx=2, bg='azure3')
        container4_1_5.pack(side='left', fill='both', padx=1)
        tk.Label(container4_1_5, text='Селезінкова вежа у\nворотах селезінки', font='Times 12', bg='azure3').pack(side='top', fill='x')
        container4_1_5_1 = tk.Frame(container4_1_5, padx=5, pady=5, bg='azure3')
        container4_1_5_1.pack(side='top', pady=2, fill='both')
        ttk.Entry(container4_1_5_1, font='Times 12', textvariable=self.var[28], width=8).pack(side='left', padx=1)
        tk.Label(container4_1_5_1, text=' мм', font='Times 12', bg='azure3').pack(side='left', fill='x')

        container5 = tk.Frame(self, padx=9)
        container5.pack(side='top', pady=2)

        self.textArea = tk.Text(container5, font='Times 11', padx=3, width=120, height=5)
        self.textArea.grid(row=0, column=0, columnspan=8)

        ttk.Button(container5, text='  Продовжити  ',
                   style='my.TButton', command=self.continueBtn).grid(row=1, column=7)

    def continueBtn(self):
        doc = DocxTemplate('tmps/tmp2.docx')
        cfg = config.Config('configs/config.cfg')
        print(self.var[2].get() + self.var[3].get())
        context = {
            'patientName': self.patientData[0].get(),
            'birthDate': self.patientData[1].get(),
            'visitDate': date.today(),
            'deviceName': cfg['deviceName'],
            'leftSize1': self.var[0].get(),
            'rightSize1': self.var[1].get(),
            'cont1': self.var[2].get() + self.var[3].get(),
            'krai': self.var[4].get(),
            'es1': self.var[5].get(),
            'eg1': self.var[6].get(),
            'vv': self.var[7].get(),
            'npv': self.var[8].get(),
            'hol': self.var[9].get(),
            'jm': self.var[10].get(),
            'size2': self.var[11].get(),
            'cont2': self.var[13].get() + self.var[14].get(),
            'borders': self.var[12].get(),
            'pz': self.var[15].get() + self.var[16].get(),
            'size3': self.var[17].get() + 'x' + self.var[18].get() + 'x' + self.var[19].get(),
            'es2': self.var[20].get(),
            'eg2': self.var[21].get(),
            'pp': self.var[22].get(),
            'size4': self.var[23].get(),
            'cont3': self.var[24].get() + self.var[25].get(),
            'es3': self.var[26].get(),
            'eg3': self.var[27].get(),
            'sv': self.var[28].get(),
            'conclu': self.textArea.get(1.0, tk.END),
            'doctorName': cfg['doctorName']
        }
        doc.render(context)
        doc.save('final.docx')
        try:
            os.system('libreoffice6.4 ' + './final.docx')
            os.system('start ' + './final.docx')
        except err:
            print(err)

    def setInfo(self, patientData, diagData):
        self.patientData = patientData
        self.diagData = diagData
        

        

    def setInfo(self, patientData, diagData):
        self.patientData = patientData
        self.diagData = diagData

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text='Сторінка 3', bg='mint cream')
        label.pack(side='top')

    def setInfo(self, patientData, diagData):
        self.patientData = patientData
        self.diagData = diagData

class DiagnosticInput(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # label = tk.Label(
            # self, text=' Ввід даних про обстеження ',
            # font='Times 15', bg='mint cream')
        # label.pack(side='top')

        self.config(bg='mint cream', padx=5, pady=5)
        self.p1 = Page1(self)
        self.p2 = Page2(self)
        self.p3 = Page3(self)

        container = tk.Frame(self, bg='mint cream')
        container.pack(side='top', fill='both', expand=True)
        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.p2.show()

    def setInfo(self, userDate, diagData):
        self.p1.setInfo(userDate, diagData)
        self.p2.setInfo(userDate, diagData)
        self.p3.setInfo(userDate, diagData)
