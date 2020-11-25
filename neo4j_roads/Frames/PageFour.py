try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame("PageThree")).place(x=20, y=50)

        self.titleLabel = tk.Label(self, text="Название:", font=controller.title_font,justify = "left")
        self.addressLabel = tk.Label(self, text="Адрес:", font=controller.title_font)
        self.dateLabel = tk.Label(self, text="Дата:", font=controller.title_font)
        self.typeLabel = tk.Label(self, text="Вид:", font=controller.title_font)

        self.titleLabel.place(x=400,y=250)
        self.addressLabel.place(x=400, y=300)
        self.dateLabel.place(x=400, y=350)
        self.typeLabel.place(x=400, y=400)