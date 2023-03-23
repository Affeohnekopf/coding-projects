from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
LISTE = [4, 8]
SCORE = 0


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        tk = self.window
        tk.config(padx= 20, pady= 20, width=340, height=450, bg=THEME_COLOR)
        tk.title("QUIZLLER")
        # Text mitte mit canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 120, text="LOOOL", font=FONT, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # Score
        self.score_scoreboard = Label(text=f"Score: {self.score}", bg=THEME_COLOR, highlightcolor="white", fg="white")
        self.score_scoreboard.grid(column=1, row=0)

        # Buttons
        img_right = PhotoImage(file="images/true.png")
        img_wrong = PhotoImage(file="images/false.png")
        button_right = Button(image=img_right, highlightthickness=0, command=self.button_correct)
        button_right.grid(column=0, row=2)
        button_wrong = Button(image=img_wrong, highlightthickness=0, command=self.button_false)
        button_wrong.grid(column=1, row=2)

        self.get_next_question()

        tk.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.canvas.config(bg="white")

    def button_correct(self):
        if self.quiz.check_answer():
            self.score += 1
            self.give_feedback_right()
        else:
            self.give_feedback_wrong()
        self.score_scoreboard.config(text=f"Score: {self.score}")

    def button_false(self):
        if not self.quiz.check_answer():
            self.score += 1
        self.score_scoreboard.config(text=f"Score: {self.score}")

    def give_feedback_wrong(self):
        self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question())

    def give_feedback_right(self):
        self.canvas.config(bg="green")
        self.window.after(1000)
