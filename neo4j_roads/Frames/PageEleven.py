from main import example
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageEleven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        def back():
            if self.index == 0:
                controller.show_frame("PageTwo")
            else: controller.show_frame("PageThirten")

        self.titleFrameLabel = tk.Label(self, text="Gorod", font=controller.title_font)
        self.titleFrameLabel.place(x=70, y=50)
        tk.Button(self, text="Назад",
                  command=lambda: back()).place(x=20, y=50)

        def callback(*args):
            date = self.variable1.get() if self.variable1.get() != "Не выбрано" else ""
            type = self.variable2.get() if self.variable2.get() != "Не выбрано" else ""
            address = self.variable3.get() if self.variable3.get() != "Не выбрано" else ""
            self.mylist.delete(0, tk.END)
            for line in example.get_works_by_filter(date, type, address):
                self.mylist.insert(tk.END,
                                   "ИД: " + str(line).split('|')[0] + " - " + str(line).split('|')[1] + " по адресу:" +
                                   str(line).split('|')[2])


        self.variable1 = tk.StringVar(self)
        self.variable1.set("one")  # default value
        self.variable1.trace("w", callback)
        self.w1 = tk.OptionMenu(self, self.variable1, "one", "two", "three")
        self.w1.config(width=10,justify=tk.LEFT,wraplength=100)
        self.w1.place(x=400,y=100)

        self.variable2 = tk.StringVar(self)
        self.variable2.set("one")  # default value
        self.variable2.trace("w", callback)
        self.w2 = tk.OptionMenu(self, self.variable2, "one", "two", "three")
        self.w2.config(width=10,justify=tk.LEFT,wraplength=100)
        self.w2.place(x=520, y=100)

        self.variable3 = tk.StringVar(self)
        self.variable3.set("one")  # default value
        self.variable3.trace("w", callback)
        self.w3 = tk.OptionMenu(self, self.variable3, "one", "two", "three")
        self.w3.config(width=10,justify=tk.LEFT,wraplength=100)
        self.w3.place(x=640, y=100)

        self.index = 0

        tk.Label(self, text="Фильтр",font=controller.title_font).place(x=620, y=50)

        frameList = tk.Frame(self)
        frameList.place(x=0, y=50)
        frameList.pack(expand=1, fill="x")

        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right", fill="y")

        def onSelectWork(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = str(w.get(index))
            id_work = int(value.split(' ', 2)[1])
            if(self.index == 0):
                controller.frames['PageFour'].show_details(id_work)
                controller.frames['PageFour'].index = 11
                controller.show_frame("PageFour")
            elif self.index == 15:
                controller.frames['PageFifteen'].show_details(id_work)
                controller.show_frame('PageFifteen')
            elif self.index == 17:
                controller.frames['PageSeventeen'].show_details(id_work)
                controller.show_frame('PageSeventeen')
            print('You selected item %d: "%s"' % (index, value))

        self.mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)
        self.mylist.bind('<<ListboxSelect>>', onSelectWork)

        #for line in range(100):
            #self.mylist.insert(tk.END, "!This is line number " + str(line))

        self.mylist.pack(side="left", fill="both", expand=1)
        scrollbar.config(command=self.mylist.yview)

    def change_list(self,date,type,address):
        self.mylist.delete(0,tk.END)
        for line in example.get_works_by_filter(date,type,address):
            self.mylist.insert(tk.END, "ИД: " + str(line).split('|')[0] + " - " + str(line).split('|')[1] + " по адресу:" + str(line).split('|')[2])

    def update_filters(self):
        str_none = "Не выбрано"

        optionList1 = [str_none] + example.get_all_dates()
        self.variable1.set(optionList1[0])
        menu = self.w1["menu"]
        menu.delete(0, "end")
        for string in optionList1:
            menu.add_command(label=string,
                             command=lambda value=string: self.variable1.set(value))

        optionList2 = [str_none] + example.get_all_types()
        self.variable2.set(optionList2[0])
        menu = self.w2["menu"]
        menu.delete(0, "end")
        for string in optionList2:
            menu.add_command(label=string,
                             command=lambda value=string: self.variable2.set(value))

        optionList3 = [str_none] + example.get_all_addresses()
        self.variable3.set(optionList3[0])
        menu = self.w3["menu"]
        menu.delete(0, "end")
        for string in optionList3:
            menu.add_command(label=string,
                             command=lambda value=string: self.variable3.set(value))
