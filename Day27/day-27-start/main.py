from tkinter import *

def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Test")
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

button2 = Button(text="Click Me 2")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)



window.mainloop()
