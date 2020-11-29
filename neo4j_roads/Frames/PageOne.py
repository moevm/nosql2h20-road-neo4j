try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def onGuestClick():
            controller.frames["PageTwo"].change_list_of_cities()
            controller.show_frame("PageTwo")

        label = tk.Label(self, text="Планирование дорожных работ", font=controller.title_font).place(x=270,y=100)

        button1 = tk.Button(self, text="Войти как гость",
                            command=lambda: onGuestClick()).place(x=350,y=250)
        button2 = tk.Button(self, text="Войти как администратор",
                            command=lambda: controller.show_frame("PageTwelve")).place(x=320,y=350)