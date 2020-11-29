try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageThirten(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Button(self, text="Редактировать дорожную работу",command=lambda: controller.show_frame("PageSeventeen")).place(x=320, y=150)
        tk.Button(self, text="Добавить дорожную работу",command=lambda: controller.show_frame("PageSixteen")).place(x=320, y=200)
        tk.Button(self, text="Удалить дорожную работу",command=lambda: controller.show_frame("PageFifteen")).place(x=320, y=250)
        tk.Button(self, text="Статистика").place(x=320, y=300)
        tk.Button(self, text="Выйти",command=lambda: controller.show_frame("PageTwelve")).place(x=320, y=400)