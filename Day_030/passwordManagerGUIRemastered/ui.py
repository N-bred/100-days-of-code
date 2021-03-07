import tkinter as tk
import math


def initializeWindow():
    window = tk.Tk()
    window.title = "Password Manager"
    window.config(padx=20, pady=20, bg="#ffffff")
    return window


def initializeCanvas(width, height):
    lock_image = tk.PhotoImage(file="logo.png")
    canvas = tk.Canvas(width=width, height=height, bg="#ffffff")
    canvas.create_image(math.floor(width/2),
                        math.floor(height/2), image=lock_image)
    canvas.image = lock_image
    canvas.grid(column=1, row=0)
    return canvas


def initializeLabels():
    website_label = tk.Label(text="Website")
    website_label.grid(column=0, row=1)

    email_label = tk.Label(text="Email/Username")
    email_label.grid(column=0, row=2)

    password_label = tk.Label(text="Password")
    password_label.grid(column=0, row=3)

    length_of_password = tk.Label(text="Length of Password")
    length_of_password.grid(column=0, row=4)

    return {"website_label": website_label, "email_label": email_label, "length_of_password": length_of_password}


def initializeInputs():
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

    return {
        "website_input": website_input,
        "email_input": email_input,
        "password_input": password_input,
        "length_of_password_input": length_of_password_input
    }


def initializeButtons(search_data, generate_password, save_password, website_input, length_of_password_input, email_input, allow_uppercase, allow_symbols, allow_numbers, password_input):
    search_button = tk.Button(
        text="Search", command=lambda: search_data(website_input=website_input))
    search_button.grid(column=2, row=1)

    generate_password_button = tk.Button(
        text="Generate Password", command=lambda: generate_password(length_of_password=length_of_password_input, allow_uppercase=allow_uppercase, allow_symbols=allow_symbols, allow_numbers=allow_numbers, password_input=password_input))
    generate_password_button.grid(column=2, row=3)

    add_password_button = tk.Button(
        text="Add", width=35, command=lambda: save_password(website_input=website_input, email_input=email_input, password_input=password_input, length_of_password_input=length_of_password_input))
    add_password_button.grid(column=1, row=8)

    return {
        "search_button": search_button,
        "generate_password_button": generate_password_button,
        "add_password_button": add_password_button
    }


def initializeCheckboxes():
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

    return {
        "allow_numbers": allow_numbers,
        "allow_symbols": allow_symbols,
        "allow_uppercase": allow_uppercase
    }


def initializeUi(width, height, search_data, generate_password, save_password):
    window = initializeWindow()
    canvas = initializeCanvas(width=width, height=height)
    labels = initializeLabels()
    inputs = initializeInputs()
    checkboxes = initializeCheckboxes()
    buttons = initializeButtons(search_data=search_data, generate_password=generate_password, save_password=save_password, website_input=inputs["website_input"], length_of_password_input=inputs["length_of_password_input"], email_input=inputs[
                                "email_input"], password_input=inputs["password_input"], allow_uppercase=checkboxes["allow_uppercase"], allow_symbols=checkboxes["allow_symbols"], allow_numbers=checkboxes["allow_numbers"])

    return window
