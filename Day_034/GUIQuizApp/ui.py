from tkinter import *

THEME_COLOR = "#375362"


class Ui:
    def __init__(self):
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

    def set_labels(self):
        self.score_label = Label(text=f"Score: ", font=(
            "Arial", 16, "bold"), fg="#fff", bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

    def set_score(self, score):
        self.score_label.config(text=f"Score: {score}")

    def set_canvas(self):
        self.canvas = Canvas(bg="#fff", height=250, width=300)
        self.canvas_text = self.canvas.create_text(
            300/2, 250/2, fill="black", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20)

    def set_canvas_text(self, text):
        self.canvas.itemconfig(self.canvas_text, text=text)

    def set_buttons(self):
        self.correct_img = PhotoImage(file="images\\true.png")
        self.incorrect_img = PhotoImage(file="images\\false.png")
        self.correct_button = Button(image=self.correct_img)
        self.incorrect_button = Button(image=self.incorrect_img)
        self.correct_button.img = self.correct_img
        self.incorrect_button.img = self.incorrect_img
        self.correct_button.grid(column=0, row=2, pady=20, padx=20)
        self.incorrect_button.grid(column=1, row=2,  pady=20, padx=20)

    def set_buttons_command(self, cmd1, cmd2):
        self.correct_button.config(command=cmd1)
        self.incorrect_button.config(command=cmd2)

    def main_loop(self):
        self.window.mainloop()
