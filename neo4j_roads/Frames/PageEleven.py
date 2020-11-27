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


        self.titleFrameLabel = tk.Label(self, text="Gorod", font=controller.title_font)
        self.titleFrameLabel.place(x=70, y=50)
        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame("PageTwo")).place(x=20, y=50)

        self.variable1 = tk.StringVar(self)
        self.variable1.set("one")  # default value
        self.w1 = tk.OptionMenu(self, self.variable1, "one", "two", "three").place(x=500,y=100)
        print(self.w1)
        print("con")
        self.variable2 = tk.StringVar(self)
        self.variable2.set("one")  # default value
        self.w2 = tk.OptionMenu(self, self.variable2, "one", "two", "three").place(x=600, y=100)

        self.variable3 = tk.StringVar(self)
        self.variable3.set("one")  # default value
        self.w3 = tk.OptionMenu(self, self.variable3, "one", "two", "three").place(x=700, y=100)

        tk.Label(self, text="Фильтр",font=controller.title_font).place(x=620, y=50)

        frameList = tk.Frame(self)
        frameList.place(x=0, y=50)
        frameList.pack(expand=1, fill="x")

        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right", fill="y")

        def onSelectWork(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            controller.show_frame("PageFour")
            print('You selected item %d: "%s"' % (index, value))

        mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)
        mylist.bind('<<ListboxSelect>>', onSelectWork)

        for line in range(100):
            mylist.insert(tk.END, "!This is line number " + str(line))

        mylist.pack(side="left", fill="both", expand=1)
        scrollbar.config(command=mylist.yview)

    def update_filters(self):
        str_none = "Не выбрано"
        optionList = [str_none] + example.get_all_dates()
        self.variable1.set(optionList[0])
        self.w1.destroy()
        self.w1 = tk.OptionMenu(self, self.variable1, *optionList).place(x=620,y=100)
