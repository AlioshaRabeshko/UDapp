import tkinter as tk
from tkinter import ttk
from page import Page
import json


class Settings(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg='mint cream')
        label = tk.Label(self, text='Налаштування',
                         font='Times 20', bg='mint cream')
        label.pack(side='top')

        with open('configs/config.json', encoding='utf-8') as json_file:
            data = json.load(json_file)

        container = tk.Frame(self, bg='azure3', pady=5, padx=10)
        container.pack(side='top', pady=3)

        container1 = tk.Frame(container, bg='azure3', pady=5, padx=10)
        container1.pack(side='top', pady=3)
        var1 = tk.StringVar()
        tk.Label(container1, text='Ім\'я лікаря: ',
                 font='Times 14', bg='azure3').pack(side='left')
        entr = ttk.Entry(container1, textvariable=var1,
                         font='Times 14')
        entr.insert(0, data['doctorName'])
        entr.pack(side='left', padx=5)

        def tmp1():
            data['doctorName'] = var1.get()
            with open('configs/config.json', 'w') as f:
                f.write(json.dumps(data))
        ttk.Button(container1, text='Зберегти',
                   command=tmp1).pack(side='left')

        container2 = tk.Frame(container, bg='azure3', pady=5, padx=10)
        container2.pack(side='top', pady=3)
        var2 = tk.StringVar()
        tk.Label(container2, text='Назва апарату УЗД: ',
                 font='Times 14', bg='azure3').pack(side='left')
        entr2 = ttk.Entry(container2, textvariable=var2,
                          font='Times 14')
        entr2.insert(0, data['deviceName'])
        entr2.pack(side='left', padx=5)

        def tmp2():
            data['deviceName'] = var2.get()
            with open('configs/config.json', 'w') as f:
                f.write(json.dumps(data))
        ttk.Button(container2, text='Зберегти',
                   command=tmp2).pack(side='left')
