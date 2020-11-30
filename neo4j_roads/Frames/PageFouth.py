from main import example
from pandas import DataFrame
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class PageFouth(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frameTitleLabel = tk.Label(self, text="Статистика", font=controller.title_font, wraplength=450,
                                        justify="left").place(x=100, y=50)
        tk.Button(self, text="Назад",command=lambda: controller.show_frame("PageThirten")).place(x=20, y=50)



    def draw_stat(self):
        f = Figure(figsize=(4, 4), dpi=100)
        a = f.add_subplot(111)
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        works_count = []
        for x in months:
            month = str(x)
            if len(month)==1:
                month = "0"+month
            works_count.append(example.get_count_works_by_month(month))

        a.plot(months, works_count)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=150)
        a.set_title('Работы по месяцам')

        cityArray = example.get_cities()
        worksPerCityArray = []

        for x in cityArray:
            worksPerCityArray.append(example.get_count_works_by_city(x))

        data1 = {'Города': cityArray,
                 'Кол-во_работ': worksPerCityArray
                 }
        df1 = DataFrame(data1, columns=['Города', 'Кол-во_работ'])
        figure1 = Figure(figsize=(5, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self)
        bar1.get_tk_widget().place(x=400, y=0)
        df1 = df1[['Города', 'Кол-во_работ']].groupby('Города').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Работы по городам')



