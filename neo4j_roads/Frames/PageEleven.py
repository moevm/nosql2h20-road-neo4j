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
        tk.Button(self, text="Фильт").place(x=720, y=50)

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


