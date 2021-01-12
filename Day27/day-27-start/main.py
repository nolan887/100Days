# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height=500)
#
# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
#
#
# window.mainloop()

def add(*args):
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 10, 15, 150, 345, 235, 3254))