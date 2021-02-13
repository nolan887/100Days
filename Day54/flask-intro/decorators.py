import time

# Introduction to decorators
def delay_decorator(function):
    def wrapper_function():
        print("waiting 2 seconds")
        time.sleep(2)
        print("done waiting")
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

def say_goodbye():
    print("bye")

say_hello()
say_goodbye()