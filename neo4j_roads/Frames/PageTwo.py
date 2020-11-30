from main import example
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

        def onListsButtonsClick(index,title):
            controller.frames["PageFive"].change_list(index)
            controller.frames["PageFive"].titleFrameLabel['text'] = title
            controller.show_frame("PageFive")

        def onFullListsButtonsClick(title):
            controller.frames["PageEleven"].update_filters()
            controller.frames["PageEleven"].change_list("","","")
            controller.frames["PageEleven"].index = 0
            controller.frames["PageEleven"].titleFrameLabel['text'] = title
            controller.show_frame("PageEleven")

        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame("PageOne")).place(x=20, y=50)
        tk.Button(self, text="Выбор по дате",
                  command=lambda: onListsButtonsClick(5,"Выбор по дате")).place(x=620, y=50)
        tk.Button(self, text="Выбор по типу",
                  command=lambda: onListsButtonsClick(7,"Выбор по типу")).place(x=670, y=50)
        tk.Button(self, text="Выбор по адресу",
                  command=lambda: onListsButtonsClick(9,"Выбор по адресу")).place(x=720, y=50)
        tk.Button(self, text="Общий список",
                  command=lambda: onFullListsButtonsClick("Общий список")).place(x=720, y=550)

        frameList = tk.Frame(self)
        frameList.place(x=0,y=0)
        frameList.pack(side="top",expand=1,fill="x")

        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right",fill="y")

        def onSelectCity(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            controller.frames["PageThree"].titleFrameLabel['text'] = value
            controller.frames["PageThree"].change_list_of_works()
            controller.show_frame("PageThree")
            print('You selected item %d: "%s"' % (index, value))

        self.mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)
        self.mylist.bind('<<ListboxSelect>>',onSelectCity)

        #for line in example.get_cities():
            #self.mylist.insert(tk.END, str(line))

        self.mylist.pack(side="left", fill="both",expand = 1)
        scrollbar.config(command=self.mylist.yview)

    def change_list_of_cities(self):
        #example.get_works_by_filter("12.12.2020","Содержание автомобильных дорог и дорожных сооружений","")
        self.mylist.delete(0,tk.END)
        for line in example.get_cities():
            self.mylist.insert(tk.END, str(line))