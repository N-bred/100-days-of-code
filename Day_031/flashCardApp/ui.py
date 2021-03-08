import tkinter as tk
from main import pick_random_string

WIDTH, HEIGHT = 800, 526
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'

window = tk.Tk()
window.title = "FlashCards App"

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = tk.Canvas(width=WIDTH, height=HEIGHT,
                   bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = tk.PhotoImage(file=r"images\\card_front.png")
back_card_image = tk.PhotoImage(file=r"images\\card_back.png")
canvas.front_image = front_card_image
canvas.back_image = back_card_image

card_image = canvas.create_image(400, 263, image=front_card_image)

language_text = canvas.create_text(
    400, 150, font=(FONT_NAME, 40, "italic"), text="French")
word_text = canvas.create_text(400, 263, font=(
    FONT_NAME, 60, "bold"), text="Trouve")

canvas.grid(column=0, row=0, columnspan=2)


wrong_image = tk.PhotoImage(file=r"images\\wrong.png")
right_image = tk.PhotoImage(file=r"images\\right.png")

wrong_button = tk.Button(
    image=wrong_image, highlightthickness=0, command=pick_random_string)
wrong_button.image = wrong_image
wrong_button.grid(column=0, row=1)

right_button = tk.Button(image=right_image, highlightthickness=0)
right_button.image = right_image
right_button.grid(column=1, row=1)


# UI methods

def change_language_text(text):
    language_text.config(text=text)


def change_word_text(text):
    word_text.config(text=text)
