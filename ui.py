from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20 ,"italic")
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,highlightthickness=0, border=0)
        self.question_text = self.canvas.create_text(150,125, text="blablabla", font=FONT, fill=THEME_COLOR, width= 280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file= r".\images\false.png")
        true_img = PhotoImage(file= r".\images\true.png")

        self.false_btn = Button(image=false_img,pady=20,bd=0,highlightthickness=0,command=self.false_ans)
        self.true_btn = Button(image=true_img,pady=20,bd=0,highlightthickness=0,command= self.true_ans)

        self.false_btn.grid(row=2, column=0)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_ans(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_ans(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

