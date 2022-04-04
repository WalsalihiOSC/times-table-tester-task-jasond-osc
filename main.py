from tkinter import *

class Cities:
    def __init__ (self):
        self.cities = ["Wellington", "Hamilton", "Auckland", "Christchurch"]

    def get_cities(self):
        return self.cities

    def capital_city(self) :
        return "Wellington"

class GUI:
    def __init__(self, parent):
        self.result = StringVar()
        self.result.set("") 

        f1 = Frame(parent)

        Label(f1, text="Question").grid(column=0)
        Label(f1, text="What is the capital of New Zealand").grid(column=1, row=0)
        self.c = Cities()
        cities = self.c.get_cities()
        
        r = 1
        for i in(cities):
            Radiobutton(f1, text=i, value=i, variable=self.result, command=self.display_result).grid(column=1, row=r, sticky=W)
            r += 1

        f1.pack()

        self.output_label = Label(parent, text=self.result.get())
        self.output_label.pack()

    def display_result(self):
        if self.result.get() == self.c.capital_city():
            self.output_label.configure(text="Correct")
        else:
            self.output_label.configure(text="Incorrect")
    
if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()
