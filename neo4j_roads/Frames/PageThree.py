from main import example
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2



class PageThree(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def onBackButtonsClick(index):
            if self.index == 0:
                controller.show_frame("PageTwo")
            else: controller.show_frame("PageFive")


        self.titleFrameLabel = tk.Label(self, text="Gorod", font=controller.title_font)
        self.titleFrameLabel.place(x=70, y=50)
        tk.Button(self, text="Назад",
                  command=lambda: onBackButtonsClick(1)).place(x=20, y=50)

  
        frameList = tk.Frame(self)
        frameList.place(x=0, y=50)
        frameList.pack(expand=1, fill="x")
        scrollbar = tk.Scrollbar(frameList)
        scrollbar.pack(side="right", fill="y")

    


        def onSelectCity(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = str(w.get(index))
            id_work = int(value.split(' ',2)[1])
            controller.frames['PageFour'].show_details(id_work)
            controller.show_frame("PageFour")
            print('You selected item %d: "%s"' % (index, value))

        self.mylist = tk.Listbox(frameList, yscrollcommand=scrollbar.set)
        self.mylist.bind('<<ListboxSelect>>', onSelectCity)
        #for line in example.get_works_from_city(self.titleFrameLabel['text']):
            #self.mylist.insert(tk.END,  str(line))

        self.mylist.pack(side="left", fill="both", expand=1)
        scrollbar.config(command=self.mylist.yview)

    def change_list_of_works(self,index = 0):
        self.mylist.delete(0,tk.END)
        self.index = index
        self.worksList = []
        if index == 0:
            self.worksList = example.get_works_from_city(self.titleFrameLabel['text'])
        elif index == 5:
            self.worksList = example.get_works_by_date(self.titleFrameLabel['text'])
        elif index == 7:
            self.worksList = example.get_works_by_type(self.titleFrameLabel['text'])
        elif index == 9:
            self.worksList = example.get_works_by_address(self.titleFrameLabel['text'])
        for line in self.worksList:
            self.mylist.insert(tk.END,"ИД: " + str(line).split('|')[0] + " - " + str(line).split('|')[1] + " по адресу:" + str(line).split('|')[2])



