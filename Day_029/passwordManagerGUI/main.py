import tkinter as tk
import math
from passwordGenerator import create_random_password

WIDTH, HEIGHT = 200, 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    random_password = create_random_password()
    password_input.delete(0, tk.END)
    password_input.insert(0, random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    text = '|'.join(
        [website_input.get(), email_input.get(), password_input.get()])
    with open("saved_passwords.txt", "a+") as file:
        file.writelines(text + "\n")
        file.close()
    clear_inputs()


def clear_inputs():
    website_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    password_input.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title = "Password Manager"
window.config(padx=20, pady=20, bg="#ffffff")

lock_image = tk.PhotoImage(file="logo.png")


canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="#ffffff")
canvas.create_image(math.floor(WIDTH/2),
                    math.floor(HEIGHT/2), image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_input = tk.Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = tk.Entry(width=35)
email_input.grid(column=1, row=2)
email_input.insert(tk.END, "dummyemail@gmail.com")

password_input = tk.Entry(width=35)
password_input.grid(column=1, row=3)


# Buttons
generate_password_button = tk.Button(
    text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = tk.Button(text="Add", width=35, command=save_password)
add_password_button.grid(column=1, row=4)


window.mainloop()
