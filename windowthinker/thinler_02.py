import tkinter as tk


class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there =tk.Button(self)

root =tk.Tk()
app =Application(master=root)
app.mainloop()
