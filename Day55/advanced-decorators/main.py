class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print("Not logged in.")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Charlie")
create_blog_post(new_user)

new_user.is_logged_in = True
create_blog_post(new_user)

# ---------- Exercise 55-1 ---------- #

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"Function {function.__name__} was called with arguments: {args}")
        result = function(args[0], args[1], args[2])
        print(f"This function with arguments returned {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(10, 3, 14)