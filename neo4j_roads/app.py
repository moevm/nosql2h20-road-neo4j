from Frames.PageOne import PageOne
from Frames.PageTwo import PageTwo
from Frames.PageThree import PageThree
from Frames.PageFour import PageFour
from Frames.PageEleven import PageEleven
from Frames.PageFive import PageFive
from Frames.PageTwelve import PageTwelve
from Frames.PageThirten import PageThirten
from Frames.PageFifteen import PageFifteen
from Frames.PageSixteen import PageSixteen
from Frames.PageSeventeen import PageSeventeen
from Frames.PageFouth import PageFouth
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=17, weight="bold")
        self.title("Планирование дорожных работ")
        container = tk.Frame(self)
        container.place(x=0,y=0)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne, PageTwo, PageThree, PageFour,PageFive, PageEleven, PageTwelve, PageThirten, PageFifteen, PageSixteen, PageSeventeen, PageFouth):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()