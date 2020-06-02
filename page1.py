import tkinter as tk
from tkinter import ttk
from page import Page


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg='mint cream')
        label = tk.Label(self, text="Знайти пацієнта в базі",
                         font='Times 20', bg='mint cream')
        label.pack(side="top")

        # Name input
        self.patientName = tk.StringVar()
        inputFrame = tk.Frame(self, bg='mint cream')
        name = tk.Label(inputFrame, text="ПІБ: ",
                        font='Times 15', bg='mint cream')
        message_entry = ttk.Entry(
            inputFrame, textvariable=self.patientName, font='Times 15')

        # Search button
        s = ttk.Style()
        s.configure('my.TButton', font=('Times', 14))
        findButton = ttk.Button(
            inputFrame, text="  Пошук піцієнтів  ", style='my.TButton', command=self.fillList)

        # Names list
        listFrame = tk.Frame(self, bg='mint cream')
        self.listBox = tk.Listbox(
            listFrame, width=30, height=20, font='Times 12')

        # Pack widgets
        name.pack(side='left')
        message_entry.pack(side='left', padx=10, pady=10)
        inputFrame.pack(side='top', padx=20, anchor='nw')
        findButton.pack(side='left')
        listFrame.pack(side='left', expand=1, anchor='nw')
        self.listBox.pack(padx=20, pady=20)

    def fillList(self):
        self.listBox.delete(0, tk.END)
        for i in range(int(self.patientName.get())):
            self.listBox.insert(tk.END, f'  {i}\t{i**i}')
