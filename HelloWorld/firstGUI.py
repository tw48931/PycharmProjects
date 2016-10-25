# coding=utf-8
from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!\n宋震天')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.quitButton.pack()
        self.quitButton1 = Button(self, text='quit1', command=self.quit)
        self.quitButton1.pack()


app = Application()
app.master.title('宋震天的第一个GUI')
app.mainloop()

