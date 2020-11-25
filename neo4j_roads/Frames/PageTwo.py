try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Меню", font=controller.title_font).place(x=70,y=50)
        tk.Label(self, text="Выберите город", font=controller.title_font).place(x=20, y=150)

        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame("PageOne")).place(x=20, y=50)
        tk.Button(self, text="5",
                  command=lambda: controller.show_frame("PageOne")).place(x=720, y=50)
        tk.Button(self, text="7",
                  command=lambda: controller.show_frame("PageOne")).place(x=670, y=50)
        tk.Button(self, text="9",
                  command=lambda: controller.show_frame("PageOne")).place(x=620, y=50)
        tk.Button(self, text="11",
                  command=lambda: controller.show_frame("PageEleven")).place(x=720, y=550)



        frameList = tk.Frame(self)
        frameList.place(x=0,y=0)
        frameList.pack(side="top",expand=1,fill="x")

        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right",fill="y")

        def onSelectCity(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            controller.show_frame("PageThree")
            controller.frames["PageThree"].titleFrameLabel['text'] = value
            print('You selected item %d: "%s"' % (index, value))

        mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)
        mylist.bind('<<ListboxSelect>>',onSelectCity)

        for line in range(100):
            mylist.insert(tk.END, "This is line number " + str(line))

        mylist.pack(side="left", fill="both",expand = 1)
        scrollbar.config(command=mylist.yview)