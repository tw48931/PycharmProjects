from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWidgets()

    def creatWidgets(self):
        self.mingZi = Entry(self)
        self.mingZi.pack()
        self.alterButton = Button(self, text='Hello', command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.mingZi.get() or 'sb'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('GUI')
app.mainloop()