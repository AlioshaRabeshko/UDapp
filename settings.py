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
            print(data)

            container1 = tk.Frame(self, bg='azure3', pady=5)
            container1.pack(side='top', pady=3)
            container1_1 = tk.Frame(container1, bg='azure3', padx=5)
            container1_1.pack(side='top', pady=3)
            tk.Label(container1_1, text='Ім\'я лікаря: ', font='Times 14', bg='azure3').pack(side='left')
            tk.Label(container1_1, text=data['doctorName'], font='Times 14', bg='azure3').pack(side='left')
            container1_2 = tk.Frame(container1, bg='azure3', padx=20, pady=5)
            container1_2.pack(side='top', pady=3)
            var1=tk.StringVar()
            tk.Label(container1_2, text='Змінити: ', font='Times 14', bg='azure3').pack(side='left')
            ttk.Entry(container1_2, textvariable=var1, font='Times 14').pack(side='left', padx=5)
            def tmp1():
                data['doctorName']=var1.get()
            ttk.Button(container1_2, text='Зберегти', command=tmp1).pack(side='left')

            container2 = tk.Frame(self, bg='azure3', padx=20, pady=20)
            container2.pack(side='top', pady=3)
            var2 = data['deviceName']
            tk.Label(container2, text='Назва апарату: ', font='Times 14', bg='azure3').pack(side='left')
            ttk.Entry(container2, textvariable=var2, font='Times 14').pack(side='left')

