try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.title("Планирование дорожных работ")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.place(x=0,y=0)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Планирование дорожных работ", font=controller.title_font).place(x=270,y=100)

        button1 = tk.Button(self, text="Войти как гость",
                            command=lambda: controller.show_frame("PageTwo")).place(x=350,y=250)
        button2 = tk.Button(self, text="Войти как администратор",
                            command=lambda: controller.show_frame("PageThree")).place(x=320,y=350)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Button(self, text="Назад",
                            command=lambda: controller.show_frame("PageOne")).place(x=20, y=50)
        tk.Label(self, text="Меню", font=controller.title_font).place(x=70,y=50)
        tk.Label(self, text="Выберите город", font=controller.title_font).place(x=20, y=150)
        tk.Button(self, text="5",
                  command=lambda: controller.show_frame("PageOne")).place(x=720, y=50)
        tk.Button(self, text="7",
                  command=lambda: controller.show_frame("PageOne")).place(x=670, y=50)
        tk.Button(self, text="9",
                  command=lambda: controller.show_frame("PageOne")).place(x=620, y=50)

        frameList = tk.Frame(self)
        frameList.place(x=0,y=200)
        frameList.pack(expand=1,fill="x")
        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right",fill="y")
        mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)

        for line in range(100):
            mylist.insert(tk.END, "This is line number " + str(line))
        mylist.pack(side="left", fill="both",expand = 1)
        scrollbar.config(command=mylist.yview)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.minsize(800,600)
    app.mainloop()