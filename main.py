import tkinter as tk
from tkinter import ttk, Canvas
from page import Page
from page1 import Page1
from settings import Settings
from diagnosticInput import DiagnosticInput



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.p1 = Page1(self)
        p2 = DiagnosticInput(self)
        self.p1.setCb(p2)

        self.settings = Settings(self)

        canvas = Canvas(self, height=2, bg='light gray')
        canvas.create_line(0, 10, 2000, 10)
        canvas.pack(side='top', fill='both')

        # Pages
        container = tk.Frame(self)
        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.settings.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        container.pack(side="top", fill="both", expand=True)

        self.p1.show()
    
    def openSettings(self):
        self.settings.lift()

    def openMain(self):
        self.p1.lift()

    def quit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    menu = tk.Menu(root)
    root.config(menu=menu)
    filemenu = tk.Menu(menu, tearoff=0)
    filemenu.add_command(label="Новый", command=main.openMain)
    filemenu.add_command(label="Налаштуваняя", command=main.openSettings)
    filemenu.add_command(label="Выход", command=root.destroy)
    helpmenu = tk.Menu(menu, tearoff=0)
    helpmenu.add_command(label="Помощь")
    helpmenu.add_command(label="О программе")
    menu.add_cascade(label="Файл", menu=filemenu)
    menu.add_cascade(label="Справка", menu=helpmenu)

    root.wm_geometry("1280x720")
    root.title('UDapp')
    root.mainloop()
