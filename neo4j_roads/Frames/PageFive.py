from main import example
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.titleFrameLabel = tk.Label(self, text="Gorod", font=controller.title_font)
        self.titleFrameLabel.place(x=70, y=50)
        tk.Button(self, text="Назад",
                  command=lambda: controller.show_frame("PageTwo")).place(x=20, y=50)

        frameList = tk.Frame(self)
        frameList.place(x=0, y=50)
        frameList.pack(expand=1, fill="x")

        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right", fill="y")

        def onSelectItem(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            controller.frames["PageThree"].titleFrameLabel['text'] = value
            controller.frames["PageThree"].change_list_of_works(self.index)
            controller.show_frame("PageThree")
            print('You selected item %d: "%s"' % (index, value))

        self.mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)
        self.mylist.bind('<<ListboxSelect>>', onSelectItem)

        #for line in range(100):
            #mylist.insert(tk.END, "PageFiveThis is line number " + str(line))

        self.mylist.pack(side="left", fill="both", expand=1)
        scrollbar.config(command=self.mylist.yview)

    def change_list(self,index):
        self.mylist.delete(0,tk.END)
        self.index = index
        if index == 5:
            for line in example.get_all_dates():
                self.mylist.insert(tk.END,str(line))
        elif index == 7:
            for line in example.get_all_types():
                self.mylist.insert(tk.END,str(line))
        elif index == 9:
            for line in example.get_all_addresses():
                self.mylist.insert(tk.END,str(line))





