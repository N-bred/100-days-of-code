import tkinter as tk
from tkinter import messagebox
import math
from passwordGenerator import create_random_password
import pyperclip

WIDTH, HEIGHT = 200, 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    random_password = create_random_password(n_of_digits=int(length_of_password_input.get()),
                                             allow_uppercase=allow_uppercase.get(),
                                             allow_symbols=allow_symbols.get(),
                                             allow_numbers=allow_numbers.get())
    password_input.delete(0, tk.END)
    password_input.insert(0, random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    if validate_inputs() is False:
        return

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    text = '|'.join([website, email, password])

    is_ok = messagebox.askokcancel(
        title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}.\nIs it ok to save?")

    if is_ok is False:
        return

    with open("saved_passwords.txt", "a+") as file:
        file.writelines(text + "\n")
        file.close()

    clear_inputs()

    pyperclip.copy(password)
    messagebox.showinfo(
        title="Copied!", message="Password copied to the clipboard!")


def validate_inputs():
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "" or int(length_of_password_input.get()) < 1:
        messagebox.showerror(title="Error", message="No empty inputs allowed")
        return False
    return True


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

length_of_password = tk.Label(text="Length of Password")
length_of_password.grid(column=0, row=4)

# Entries
website_input = tk.Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = tk.Entry(width=35)
email_input.grid(column=1, row=2)
email_input.insert(tk.END, "dummyemail@gmail.com")

password_input = tk.Entry(width=35)
password_input.grid(column=1, row=3)

length_of_password_input = tk.Entry(width=35)
length_of_password_input.grid(column=1, row=4)
length_of_password_input.insert(0, "10")

# Buttons
generate_password_button = tk.Button(
    text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = tk.Button(text="Add", width=35, command=save_password)
add_password_button.grid(column=1, row=8)

# Checkboxes
allow_numbers = tk.BooleanVar()
allow_numbers_checkbox = tk.Checkbutton(
    text="Allow numbers? ", variable=allow_numbers)
allow_numbers_checkbox.grid(column=1, row=5)

allow_symbols = tk.BooleanVar()
allow_symbols_checkbox = tk.Checkbutton(
    text="Allow symbols? ", variable=allow_symbols)
allow_symbols_checkbox.grid(column=1, row=6)

allow_uppercase = tk.BooleanVar()
allow_uppercase_checkbox = tk.Checkbutton(
    text="Allow uppercase? ", variable=allow_uppercase)
allow_uppercase_checkbox.grid(column=1, row=7)

window.mainloop()
