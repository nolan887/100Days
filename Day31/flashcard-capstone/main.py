from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
timer = None
current_card = None

# ---------------------------- CARD FUNCTIONS ------------------------------- #
def next_card():
    global current_card
    canvas.itemconfig(card_img, image=card_front_img)
    current_card = random.choice(french_dict)
    fr_word = current_card["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_word, fill="black")
    x_button.config(state=DISABLED)
    check_button.config(state=DISABLED)
    start_clock(3)

def flip_card():
    global current_card
    en_word = current_card["English"]
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=en_word, fill="white")
    x_button.config(state=NORMAL)
    check_button.config(state=NORMAL)

def knew_it():
    global current_card
    french_dict.remove(current_card)

    data = pandas.DataFrame(french_dict)
    data.to_csv("./data/unknown_words.csv", index=False)

    next_card()

def keep_learning():
    next_card()

# ---------------------------- TIMER FUNCTION ------------------------------- #
def start_clock(count):
    if count > 0:
        global timer
        timer = window.after(1000, start_clock, count-1)
    else:
        flip_card()

# --------------------------- CARD SETUP ------------------------------ #
# Read Dictionary CSV
try:
    french_data = pandas.read_csv("./data/unknown_words.csv")
except FileNotFoundError:
    french_data = pandas.read_csv("./data/french_words.csv")
finally:
    french_dict = french_data.to_dict(orient="records")

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
card_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 158, text="Title", font=LANG_FONT)
word_text = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# SETUP BUTTONS
x_button = Button(image=wrong_img, highlightthickness=0, command=keep_learning)
x_button.grid(row=1, column=0)

check_button = Button(image=right_img, highlightthickness=0, command=knew_it)
check_button.grid(row=1, column=1)

# START STUDYING
next_card()

# KEEP PROGRAM RUNNING
window.mainloop()
