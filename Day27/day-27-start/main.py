import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


# Making Labels
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# Both of the following two lines do the same thing
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Buttons

def button_click():
    print("I got clicked")
    # my_label["text"] = "Button got Clicked"
    # my_label.pack
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_click)
button.pack()


# Entry
input = tkinter.Entry(width=10)
input.pack()



window.mainloop()
