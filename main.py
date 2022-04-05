from tkinter import *
import random

class Question():
    def __init__(self):
        self.n1 = random. randint(0,10)
        self.n2 = random. randint(0,10)

    def get(self):
        question = str(self.n1) + " * " + str(self.n2) + " = "
        return question

    def correct_answer(self):
        correct = self.n1 * self.n2
        return correct

class GUI:
    def __init__(self, parent):
        self.result = StringVar()
        self.result.set("") 

        f1 = Frame(parent)

        self.q_label = Label(f1, text="NUMBER")
        self.q_label.grid(row=0, column=0)
        self.q_entry = Entry(f1)
        self.q_entry.grid(row=0, column=1)

        Button(f1, text="Next", command=self.create_question).grid(row=0, column=2)
        Button(f1, text="Check Answer", command=self.check_question).grid(row=1, column=1)

        f1.pack()

        self.q_label.configure(text="NUMBER*NUMBER=")

    def create_question(self):
        return

    def check_question(self):
        print(self.q_entry.get())
        return
    
if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()