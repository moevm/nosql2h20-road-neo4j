from main import example
import tkinter.messagebox
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageThirten(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def onFullListsButtonsClick(title,index):
            controller.frames["PageEleven"].update_filters()
            controller.frames["PageEleven"].change_list("","","")
            controller.frames["PageEleven"].index = index
            controller.frames["PageEleven"].titleFrameLabel['text'] = title
            controller.show_frame("PageEleven")

        def onCreateButtonClick():
            controller.frames["PageSixteen"].clear_details()
            controller.show_frame("PageSixteen")

        def onStatButtonClick():
            controller.frames["PageFouth"].draw_stat()
            controller.show_frame("PageFouth")

        def importButtonClick():
            example.import_database()
            tk.messagebox.showinfo("Инфо", "Импортировано!")

        def exportButtonClick():
            example.export_database()
            tk.messagebox.showinfo("Инфо", "Экспортировано!")

        tk.Button(self, text="Импорт",command=lambda: importButtonClick()).place(x=100, y=50)
        tk.Button(self, text="Экспорт",command=lambda: exportButtonClick()).place(x=150, y=50)
        tk.Button(self, text="Редактировать дорожную работу",command=lambda: onFullListsButtonsClick("Общий список",17)).place(x=320, y=150)
        tk.Button(self, text="Добавить дорожную работу",command=lambda: onCreateButtonClick()).place(x=320, y=200)
        tk.Button(self, text="Удалить дорожную работу",command=lambda: onFullListsButtonsClick("Общий список",15)).place(x=320, y=250)
        tk.Button(self, text="Статистика",command=lambda: onStatButtonClick()).place(x=320, y=300)
        tk.Button(self, text="Выйти",command=lambda: controller.show_frame("PageTwelve")).place(x=320, y=400)