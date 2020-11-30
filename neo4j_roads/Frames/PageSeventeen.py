from main import example
import tkinter.messagebox
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageSeventeen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frameTitleLabel = tk.Label(self, text="Редактирование", font=controller.title_font, wraplength=450,
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

        def update_work():
            str1 = self.titleEnrty.get()
            str2 = self.addressEntry.get()
            str3 = self.dateEntry.get()
            str4 = self.typeEntry.get()
            if(str1 == "" or str2=="" or str3=="" or str4==""):
                tk.messagebox.showwarning("Предупреждение", "Поля не могут быть пустыми!")
            else:
                example.update_work_by_id(int(self.id_work),str1,str2,str3,str4)
                tk.messagebox.showinfo("Инфо", "Обновлено!")
                controller.frames["PageEleven"].change_list("", "", "")
                controller.show_frame("PageEleven")

        def back():
            controller.frames["PageEleven"].change_list("","","")
            controller.show_frame("PageEleven")

        tk.Button(self, text="Сохранить",command=lambda: update_work()).place(x=100, y=400)
        tk.Button(self, text="Назад",command=lambda: back()).place(x=20, y=50)

    def show_details(self,id):
        details = example.get_work_details(id).split("|")
        self.id_work = id

        self.titleEnrty.delete(0,tk.END)
        self.addressEntry.delete(0,tk.END)
        self.dateEntry.delete(0,tk.END)
        self.typeEntry.delete(0,tk.END)

        self.titleEnrty.insert(0,details[1])
        self.addressEntry.insert(0,details[2])
        self.dateEntry.insert(0,details[3])
        self.typeEntry.insert(0,details[4])