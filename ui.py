from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        """
        :param quiz_brain: Brain of our program
        """
        self.quiz = quiz_brain
        self.app = Tk()
        self.app.title("Quizzler")
        self.app.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.question_number = Label(text="Question: 1/10", fg="white", bg=THEME_COLOR)
        self.question_number.grid(row=0, column=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="", font=FONT, width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.pressed_true,
            bd=0,
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.pressed_false,
            bd=0,
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.app.mainloop()

    def get_next_question(self):
        """
        Loads next question if there is any
        """
        self.button_enable()
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.question_number.config(text=f"Question: {self.quiz.question_number + 1}/10")
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # self.question_number.config(text="No more questions.")
            self.canvas.itemconfig(self.question_text,
                                   text="Congratulation, You've reached end of the quiz.",
                                   fill=THEME_COLOR
                                   )
            self.button_disable()

    def pressed_true(self):
        """
        sends user answer when clicked on green check
        """
        self.give_feedback(self.quiz.check_answer("true"))

    def pressed_false(self):
        """
        sends user answer when clicked red cross
        """
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """
        is triggered after button press, shows user if he answered right or wrong and update score
        :param is_right: bool, True if user answered right
        """
        self.button_disable()
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")

        self.app.after(500, self.get_next_question)

    def button_disable(self):
        """
        binds buttons to do nothing
        """
        self.true_button.config(command=self.do_nothing)
        self.false_button.config(command=self.do_nothing)

    def button_enable(self):
        """
        binds buttons to function back from disabled state
        """
        self.true_button.config(command=self.pressed_true)
        self.false_button.config(command=self.pressed_false)

    def do_nothing(self):
        pass



