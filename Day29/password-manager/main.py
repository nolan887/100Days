from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    print("pw generated")
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def pw_save():
    web = str(website_entry.get())
    email = str(user_entry.get())
    pw = str(password_entry.get())
    with open("my_pw.txt", mode="a") as file:
        file.write(f"{web} | {email} | {pw}")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

# Setup WIndow
window = Tk()
window.title("Password Manager")
window.config(padx=75, pady=25)

# Setup Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Setup Labels
website_label = Label(text="Website: ", justify="right")
website_label.grid(row=1, column=0)

user_label = Label(text="E-Mail / Username: ", justify="right")
user_label.grid(row=2, column=0)

password_label = Label(text="Password: ", justify="right")
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