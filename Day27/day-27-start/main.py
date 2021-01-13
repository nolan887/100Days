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


# def add(*args):
#     print(args[2])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3, 5, 6, 10, 15, 150, 345, 235, 3254))



# KWARGS
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # This replaces the above code and protects code from crashing if there is not a kwarg assigned
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Mazda", model="3 Hatch")
print(my_car.make)
print(my_car.model)

ashleys_car = Car(model="Tiguan")
print(ashleys_car.make)
print(ashleys_car.model)

def test(*args):
    print(type(args))
    print(args)

test(1,2,3,4)