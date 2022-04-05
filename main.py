from tkinter import *
import random

class Generate_Question():
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
        self.question = StringVar()
        self.question.set(self.create_question) 

        self.q = Generate_Question()

        f1 = Frame(parent)

        self.question_label = Label(f1, text="NUMBER")
        self.question_label.grid(row=0, column=0)
        
        self.question_entry = Entry(f1)
        self.question_entry.grid(row=0, column=1)

        Button(f1, text="Next", command=self.create_question).grid(row=0, column=2)
        Button(f1, text="Check Answer", command=self.check_question).grid(row=1, column=0)

        self.result_label = Label(f1, text="")
        self.result_label.grid(row=1, column=1)

        f1.pack()

        self.question_label.configure(text=self.q.get())

    def create_question(self):
        self.q = Generate_Question()
        self.question_label.configure(text=self.q.get())

    def check_question(self):
        print(self.q.correct_answer())
        print(self.question_entry.get())
        if int(self.question_entry.get()) == self.q.correct_answer():
            self.result_label.configure(text="Correct")
        else:
            self.result_label.configure(text="Incorrect")
        return
    
if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()