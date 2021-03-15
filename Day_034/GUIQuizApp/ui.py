from os import stat
from tkinter import *

THEME_COLOR = "#375362"


class Ui:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.resizable(False, False)

        # Call methods
        self.set_labels()
        self.set_score(0)
        self.set_canvas()
        self.set_canvas_text("Heyeyeyey")
        self.set_buttons()

        # Call

        self.get_next_question()

    def set_labels(self):
        self.score_label = Label(text=f"Score: ", font=(
            "Arial", 18, "bold"), fg="#fff", bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

    def set_score(self, score: str):
        self.score_label.config(text=f"Score: {score}")

    def set_canvas(self):
        self.canvas = Canvas(bg="#fff", height=250, width=300)
        self.canvas_text = self.canvas.create_text(
            300/2, 250/2, width=280, fill="black", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20)

    def set_canvas_text(self, text):
        self.canvas.itemconfig(self.canvas_text, text=text)

    def set_buttons(self):
        correct_img = PhotoImage(file="images\\true.png")
        incorrect_img = PhotoImage(file="images\\false.png")
        self.correct_button = Button(
            image=correct_img, command=self.correct_option_btn)
        self.incorrect_button = Button(
            image=incorrect_img, command=self.incorrect_option_btn)
        self.correct_button.img = correct_img
        self.incorrect_button.img = incorrect_img
        self.correct_button.grid(column=0, row=2, pady=20, padx=20)
        self.incorrect_button.grid(column=1, row=2,  pady=20, padx=20)

    def get_next_question(self):
        self.check_if_game_over()
        self.update_ui()
        q_text = self.quiz.get_next_question()
        self.set_canvas_text(q_text)

    def correct_option_btn(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def incorrect_option_btn(self):
        self.quiz.check_answer("False")
        self.get_next_question()

    def update_ui(self):
        self.set_score(self.quiz.get_score())

    def game_over(self):
        self.set_canvas_text(f"Game Over\nYour Score: {self.quiz.get_score()}")
        self.correct_button.config(state="disable")
        self.incorrect_button.config(state="disable")

    def check_if_game_over(self):
        if self.quiz.still_has_questions() is False:
            self.game_over()

    def main_loop(self):
        self.window.mainloop()
