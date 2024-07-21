from tkinter import *

THEME_COLOR = "#375362"

class quizinterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.geometry("400x500")
        self.window.config(padx=100, pady=50, bg=THEME_COLOR)

        self.tick_image = PhotoImage(file="./images/true.png")
        self.cross_image = PhotoImage(file="./images/false.png")

        self.score = Label(text="Lorem Ipsum")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=200, height=224, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2,padx=30,pady=30)
        self.question_text = self.canvas.create_text(text="heheehhe", fill=THEME_COLOR)

        self.tick_button = Button(image=self.tick_image, highlightthickness=0)
        self.tick_button.grid(row=2, column=0)

        self.cross_button = Button(image=self.cross_image, highlightthickness=0)
        self.cross_button.grid(row=2, column=1)

        self.window.mainloop()

