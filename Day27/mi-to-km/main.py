from tkinter import *

def convert_button_click():
    miles = int(miles_entry.get())
    km = miles * 1.609344
    km = round(km,1)
    convert_label.config(text=km)

# window
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=100)
window.config(padx=45, pady=45)

# entry
miles_entry = Entry(width=10, justify="center")
miles_entry.grid(column=1, row=0)
miles_entry.focus()

# labels
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

descr_label = Label(text="is equal to")
descr_label.grid(column=0, row=1)

convert_label = Label(text="0")
convert_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# button
calc_button = Button(text="Calculate", command=convert_button_click)
calc_button.grid(column=1,row=2)

window.mainloop()