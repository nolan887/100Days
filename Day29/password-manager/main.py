from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_pass():
    password_entry.delete(0,END)
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)

    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def pw_save():
    web = str(website_entry.get())
    email = str(user_entry.get())
    pw = str(password_entry.get())

    if len(web) == 0 or len(email) == 0 or len(pw) == 0:
        messagebox.showerror(title="ERROR", message="One or more of the required fields are blank.")
        website_entry.focus()
    else:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: "
                                               f"{pw} \nIs it ok to save?")
        if is_ok:
            with open("my_pw.txt", mode="a") as file:
                file.write(f"\n{web} | {email} | {pw}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    pass


# ---------------------------- UI SETUP ------------------------------- #

# Setup Window
window = Tk()
window.title("Password Manager")
window.config(padx=75, pady=25)

# Setup Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Setup Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

user_label = Label(text="E-Mail / Username: ")
user_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Setup Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

user_entry = Entry(width=35)
user_entry.insert(0, "default@email.com")
user_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button Setup
generate_btn = Button(text="Generate Password", command=gen_pass)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", command=pw_save, width=36)
add_btn.grid(row=4, column=1, columnspan=2)

# Keep Program Open
window.mainloop()
