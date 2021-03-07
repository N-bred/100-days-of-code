import tkinter as tk
from tkinter import messagebox
import math
from passwordGenerator import create_random_password
import pyperclip
import json

WIDTH, HEIGHT = 200, 200
FILE_NAME = "saved_passwords.json"


# ---------------------------- MANAGING THE FLOW ------------------------------- #


def create_file():
    with open(FILE_NAME, "w+") as file:
        file.write(json.dumps([]))
        file.close()


def check_if_file_exists_or_create():
    try:
        with open(FILE_NAME) as file:
            json.loads(file.read())
            file.close()
    except FileNotFoundError:
        create_file()
    except json.JSONDecodeError:
        create_file()
    else:
        return True


check_if_file_exists_or_create()


def get_saved_passwords():
    file = open(FILE_NAME)
    json_data = json.loads(file.read())
    file.close()
    return json_data


saved_passwords_data = get_saved_passwords()

# ---------------------------- DATA FORMATTER ------------------------------- #


def data_formatter():
    data = {
        "website": website_input.get(),
        "email": email_input.get(),
        "password": password_input.get()
    }
    return data


def merge_data(data):
    saved_passwords_data.append(data)


def save_data_to_json():
    with open(FILE_NAME, "w+") as file:
        file.write(json.dumps(saved_passwords_data))
        file.close()

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

    data = data_formatter()

    is_ok = messagebox.askokcancel(
        title=data["website"], message=f"These are the details entered: \nEmail: {data['email']}\nPassword: {data['password']}.\nIs it ok to save?")

    if is_ok is False:
        return

    merge_data(data)
    save_data_to_json()
    clear_inputs()

    pyperclip.copy(data['password'])
    messagebox.showinfo(
        title="Copied!", message="Password copied to the clipboard!")

# ---------------------------- HANDLING INPUTS ------------------------------- #


def validate_inputs():
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "" or int(length_of_password_input.get()) < 1:
        messagebox.showerror(title="Error", message="No empty inputs allowed")
        return False
    return True


def clear_inputs():
    website_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    password_input.delete(0, tk.END)

# ---------------------------- HANDLE SEARCH ------------------------------- #


def search_in_list(arr, cb):
    for i in arr:
        if cb(i):
            return i
    raise StopIteration


def search_data():
    try:
        registry = search_in_list(
            saved_passwords_data, lambda x: True if x['website'] == website_input.get() else False)
    except StopIteration:
        return messagebox.showerror(title="Registry not found", message="The website wasn't found in the registry")
    else:
        return messagebox.showinfo(title=registry['website'], message=f"Email: {registry['email']}\nPassword: {registry['password']}")

# ---------------------------- MAIN CALLER ------------------------------- #


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
search_button = tk.Button(
    text="Search", command=search_data)
search_button.grid(column=2, row=1)

generate_password_button = tk.Button(
    text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = tk.Button(
    text="Add", width=35, command=save_password)
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
