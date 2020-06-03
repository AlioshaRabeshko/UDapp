import tkinter as tk
from tkinter import ttk, Canvas
from page import Page
from page1 import Page1


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Сторінка 2", bg='azure2')
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Сторінка 3", bg='azure2')
        label.pack(side="top", fill="both", expand=True)


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Сторінка 4")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p1.setCb(p2)

        # Buttons
        buttonframe = tk.Frame(self, bg='SlateGray1')
        buttonframe.pack(side="top", fill="x", expand=False)
        b1 = ttk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = ttk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = ttk.Button(buttonframe, text="Page 3", command=p3.lift)
        canvas = Canvas(self, height=2, bg='light gray')
        canvas.create_line(0, 10, 2000, 10)
        canvas.pack(side='top', fill='both')

        # Pages
        container = tk.Frame(self)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        container.pack(side="top", fill="both", expand=True)

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("900x600")
    root.title('UDapp')
    root.mainloop()
