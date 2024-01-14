from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, string=f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": username,
        "password": password,

    }}
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)

        else:
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"Email: {data[website]['email']}\n Password: {data[website]['password']} ")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website} found")

    #

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, )
email_label = Label(text="Username/Email:")
email_label.grid(row=3, column=0, )
password_label = Label(text="Password:")
password_label.grid(row=4, column=0, )
# entry

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.get()
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=3, column=1, columnspan=2)
username_entry.get()
password_entry = Entry(width=35, )
password_entry.get()
password_entry.grid(row=4, column=1, columnspan=2)

# buttons
generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(row=5, column=1, )
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=6, column=1, columnspan=2)
search_button = Button(text="search", command=find_password)
search_button.grid(row=2, column=1)
window.mainloop()
