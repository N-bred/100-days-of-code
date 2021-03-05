import tkinter as tk
import math

WIDTH, HEIGHT = 400, 400

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title = "Password Manager"
window.config(padx=20, pady=20, )

lock_image = tk.PhotoImage(file="logo.png")


canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.create_image(math.floor(WIDTH/2),
                    math.floor(HEIGHT/2), image=lock_image)
canvas.pack()

window.mainloop()
