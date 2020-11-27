from main import example
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
        self.index = 0
        def onBackButtonClick():
            if self.index == 11:
                controller.show_frame("PageEleven")
            else: controller.show_frame("PageThree")

        tk.Button(self, text="Назад",
                  command=lambda: onBackButtonClick()).place(x=20, y=50)

        self.titleLabel = tk.Label(self, text="Название:", font=controller.title_font,wraplength = 450,justify = "left")
        self.addressLabel = tk.Label(self, text="Адрес:", font=controller.title_font,wraplength = 450,justify="left")
        self.dateLabel = tk.Label(self, text="Дата:", font=controller.title_font,wraplength = 450,justify="left")
        self.typeLabel = tk.Label(self, text="Вид:", font=controller.title_font,wraplength = 450,justify="left")


        self.titleLabel.place(x=300,y=250)
        self.addressLabel.place(x=300, y=300)
        self.dateLabel.place(x=300, y=350)
        self.typeLabel.place(x=300, y=400)

    def show_details(self,id):
        details = example.get_work_details(id).split("|")
        self.titleLabel['text'] = details[1]
        self.addressLabel['text'] = details[2]
        self.dateLabel['text'] = details[3]
        self.typeLabel['text'] = details[4]