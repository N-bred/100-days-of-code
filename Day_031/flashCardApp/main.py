import tkinter as tk
import pandas as pd
import random

WIDTH, HEIGHT = 800, 526
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'
to_learn = {}
current_card = {}

try:
    data = pd.read_csv(r'data\\words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv(r"data\\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=front_card_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=back_card_image)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(r"data\\words_to_learn.csv", index=False)
    next_card()


# UI
window = tk.Tk()
window.title = "FlashCards App"
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = tk.Canvas(width=WIDTH, height=HEIGHT,
                   bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_image = tk.PhotoImage(file=r"images\\card_front.png")
back_card_image = tk.PhotoImage(file=r"images\\card_back.png")

canvas.front_image = front_card_image
canvas.back_image = back_card_image

card_image = canvas.create_image(400, 263, image=front_card_image)

language_text = canvas.create_text(
    400, 150, font=(FONT_NAME, 40, "italic"), text="")
word_text = canvas.create_text(400, 263, font=(
    FONT_NAME, 60, "bold"), text="")

canvas.grid(column=0, row=0, columnspan=2)


wrong_image = tk.PhotoImage(file=r"images\\wrong.png")
right_image = tk.PhotoImage(file=r"images\\right.png")

wrong_button = tk.Button(
    image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.image = wrong_image
wrong_button.grid(column=0, row=1)

right_button = tk.Button(
    image=right_image, highlightthickness=0, command=is_known)
right_button.image = right_image
right_button.grid(column=1, row=1)


next_card()

window.mainloop()
