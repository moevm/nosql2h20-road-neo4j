try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageTwelve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Вход в режим администратора", font=controller.title_font).place(x=270,y=100)

        tk.Label(self, text="Логин", font=controller.title_font).place(x=200,y=250)

        tk.Label(self, text="Пароль", font=controller.title_font).place(x=200,y=350)
        tk.Entry().place(x=350, y=250)
        tk.Entry().place(x=350, y=350)