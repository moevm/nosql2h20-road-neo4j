from main import example
import tkinter.messagebox
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

        self.frameTitleLabel = tk.Label(self, text="Добавление", font=controller.title_font, wraplength=450,
                                        justify="left").place(x=100, y=50)

        self.titleLabel = tk.Label(self, text="Название:", font=controller.title_font, wraplength=450, justify="left")
        self.addressLabel = tk.Label(self, text="Адрес:", font=controller.title_font, wraplength=450, justify="left")
        self.dateLabel = tk.Label(self, text="Дата:", font=controller.title_font, wraplength=450, justify="left")
        self.typeLabel = tk.Label(self, text="Вид:", font=controller.title_font, wraplength=450, justify="left")
        self.cityLabel = tk.Label(self, text="Город:", font=controller.title_font, wraplength=450, justify="left")

        self.titleLabel.place(x=100, y=100)
        self.addressLabel.place(x=100, y=150)
        self.dateLabel.place(x=100, y=200)
        self.typeLabel.place(x=100, y=250)
        self.cityLabel.place(x=100, y=300)

        self.titleEnrty = tk.Entry(self)
        self.addressEntry = tk.Entry(self)
        self.dateEntry = tk.Entry(self)
        self.typeEntry = tk.Entry(self)

        self.titleEnrty.place(x=200,y=100)
        self.addressEntry.place(x=200,y=150)
        self.dateEntry.place(x=200,y=200)
        self.typeEntry.place(x=200,y=250)

        self.variable1 = tk.StringVar(self)
        self.variable1.set("one")  # default value
        self.w1 = tk.OptionMenu(self, self.variable1, "one", "two", "three")
        self.w1.config(width=10, justify=tk.LEFT, wraplength=100)
        self.w1.place(x=200, y=300)

        def save_work():
            str1 = self.titleEnrty.get()
            str2 = self.addressEntry.get()
            str3 = self.dateEntry.get()
            str4 = self.typeEntry.get()
            str5 = self.variable1.get()
            if(str1 == "" or str2=="" or str3=="" or str4==""):
                tk.messagebox.showwarning("Предупреждение", "Поля не могут быть пустыми!")
            else:
                example.create_work(str1,str2,str3,str4,str5)
                tk.messagebox.showinfo("Инфо", "Добавлено!")
                controller.show_frame("PageThirten")

        tk.Button(self, text="Добавить",command=lambda:save_work()).place(x=100, y=400)
        tk.Button(self, text="Назад",command=lambda: controller.show_frame("PageThirten")).place(x=20, y=50)

    def clear_details(self):
        self.titleEnrty.delete(0, tk.END)
        self.addressEntry.delete(0, tk.END)
        self.dateEntry.delete(0, tk.END)
        self.typeEntry.delete(0, tk.END)

        optionList1 = example.get_cities()
        self.variable1.set(optionList1[0])
        menu = self.w1["menu"]
        menu.delete(0, "end")
        for string in optionList1:
            menu.add_command(label=string,
                             command=lambda value=string: self.variable1.set(value))