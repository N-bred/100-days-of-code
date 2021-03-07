from tkinter import messagebox, END
from passwordGenerator import create_random_password
import pyperclip
import json
from ui import initializeUi

WIDTH, HEIGHT = 200, 200
FILE_NAME = "saved_passwords.json"
saved_passwords_data = []
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


def get_saved_passwords():
    file = open(FILE_NAME)
    json_data = json.loads(file.read())
    file.close()
    return json_data


# ---------------------------- DATA FORMATTER ------------------------------- #


def data_formatter(website, email, password):
    data = {
        "website": website,
        "email": email,
        "password": password
    }
    return data


def merge_data(data):
    saved_passwords_data.append(data)


def save_data_to_json():
    with open(FILE_NAME, "w+") as file:
        file.write(json.dumps(saved_passwords_data))
        file.close()


def format_info_message(email, password):
    return f"Email: {email}\nPassword: {password}"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(length_of_password, allow_uppercase, allow_symbols, allow_numbers, password_input):
    random_password = create_random_password(n_of_digits=int(length_of_password.get()),
                                             allow_uppercase=allow_uppercase.get(),
                                             allow_symbols=allow_symbols.get(),
                                             allow_numbers=allow_numbers.get())
    password_input.delete(0, END)
    password_input.insert(0, random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password(website_input, email_input, password_input, length_of_password_input):
    if validate_inputs(website_input, email_input, password_input, length_of_password_input) is False:
        return

    data = data_formatter(website=website_input.get(),
                          email=email_input.get(), password=password_input.get())

    is_ok = messagebox.askokcancel(
        title=data["website"], message=f"These are the details entered: \nEmail: {data['email']}\nPassword: {data['password']}.\nIs it ok to save?")

    if is_ok is False:
        return

    merge_data(data)
    save_data_to_json()
    clear_inputs(website_input=website_input,
                 email_input=email_input, password_input=password_input)

    pyperclip.copy(data['password'])
    messagebox.showinfo(
        title="Copied!", message="Password copied to the clipboard!")

# ---------------------------- HANDLING INPUTS ------------------------------- #


def validate_inputs(website_input, email_input, password_input, length_of_password_input):
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "" or int(length_of_password_input.get()) < 1:
        messagebox.showerror(title="Error", message="No empty inputs allowed")
        return False
    return True


def clear_inputs(website_input, email_input, password_input):
    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)

# ---------------------------- HANDLE SEARCH ------------------------------- #


def search_in_list(arr, cb):
    data = [i for i in arr if cb(i)]
    if len(data) == 0:
        raise ValueError
    return data


def search_data(website_input):
    try:
        data = search_in_list(
            saved_passwords_data, lambda x: True if x['website'] == website_input.get() else False)
    except ValueError:
        return messagebox.showerror(title="Registry not found", message="The website wasn't found in the registry")
    else:
        data_string = '\n\n'.join([format_info_message(
            reg['email'], reg['password']) for reg in data])
        return messagebox.showinfo(title=data[0]['website'], message=f"{data_string}")


# ---------------------------- MAIN CALLER ------------------------------- #


def main():
    if __name__ == "__main__":
        # Initialize Data
        check_if_file_exists_or_create()
        global saved_passwords_data
        saved_passwords_data = get_saved_passwords()
        # Initialize UI
        window = initializeUi(width=WIDTH, height=HEIGHT,
                              search_data=search_data, generate_password=generate_password, save_password=save_password)

        window.mainloop()


main()
