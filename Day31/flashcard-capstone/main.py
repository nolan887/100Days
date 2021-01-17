from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")


# ---------------------------- FUNCTIONS ------------------------------- #
def knew_it():
    pass


def keep_learning():
    pass


# ---------------------------- UI SETUP ------------------------------- #
# SETUP WINDOW
window = Tk()
window.title("Flashy: Language Frequent Word Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# IMPORT IMAGE FILES
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# SETUP CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 158, text="Title", font=LANG_FONT)
canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# SETUP BUTTONS
x_button = Button(image=wrong_img, highlightthickness=0, command=keep_learning)
x_button.grid(row=1, column=0)

check_button = Button(image=right_img, highlightthickness=0, command=knew_it)
check_button.grid(row=1, column=1)

# KEEP PROGRAM RUNNING
window.mainloop()
