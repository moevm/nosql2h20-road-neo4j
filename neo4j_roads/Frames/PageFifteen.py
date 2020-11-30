from main import example
import tkinter.messagebox
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageFifteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frameTitleLabel = tk.Label(self, text="Удаление", font=controller.title_font, wraplength=450, justify="left").place(x=100, y=50)

        self.titleLabel = tk.Label(self, text="Название:", font=controller.title_font, wraplength=450, justify="left")
        self.addressLabel = tk.Label(self, text="Адрес:", font=controller.title_font, wraplength=450, justify="left")
        self.dateLabel = tk.Label(self, text="Дата:", font=controller.title_font, wraplength=450, justify="left")
        self.typeLabel = tk.Label(self, text="Вид:", font=controller.title_font, wraplength=450, justify="left")

        self.titleLabel.place(x=100, y=100)
        self.addressLabel.place(x=100, y=150)
        self.dateLabel.place(x=100, y=200)
        self.typeLabel.place(x=100, y=250)

        def delete_work():
            example.delete_work_by_id(int(self.id_work))
            tk.messagebox.showinfo("Инфо", "Удалено!")

        def back():
            controller.frames["PageEleven"].change_list("","","")
            controller.show_frame("PageEleven")

        tk.Button(self, text=" Удалить",command=lambda: delete_work()).place(x=100, y=400)
        tk.Button(self, text="Назад",command=lambda: back()).place(x=20, y=50)

    def show_details(self,id):
        details = example.get_work_details(id).split("|")
        self.id_work = id
        self.titleLabel['text'] = "Название:"+details[1]
        self.addressLabel['text'] = "Адрес:"+details[2]
        self.dateLabel['text'] = "Дата:"+details[3]
        self.typeLabel['text'] = "Вид:"+details[4]