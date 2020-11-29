try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageSixteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frameTitleLabel = tk.Label(self, text="Название:", font=controller.title_font, wraplength=450,
                                        justify="left").place(x=100, y=50)

        self.titleLabel = tk.Label(self, text="Название:", font=controller.title_font, wraplength=450, justify="left")
        self.addressLabel = tk.Label(self, text="Адрес:", font=controller.title_font, wraplength=450, justify="left")
        self.dateLabel = tk.Label(self, text="Дата:", font=controller.title_font, wraplength=450, justify="left")
        self.typeLabel = tk.Label(self, text="Вид:", font=controller.title_font, wraplength=450, justify="left")

        self.titleLabel.place(x=100, y=100)
        self.addressLabel.place(x=100, y=150)
        self.dateLabel.place(x=100, y=200)
        self.typeLabel.place(x=100, y=250)

        self.titleEnrty = tk.Entry(self)
        self.addressEntry = tk.Entry(self)
        self.dateEntry = tk.Entry(self)
        self.typeEntry = tk.Entry(self)

        self.titleEnrty.place(x=200,y=100)
        self.addressEntry.place(x=200,y=150)
        self.dateEntry.place(x=200,y=200)
        self.typeEntry.place(x=200,y=250)

        tk.Button(self, text="Добавить").place(x=100, y=400)
        tk.Button(self, text="Назад",command=lambda: controller.show_frame("PageThirten")).place(x=20, y=50)