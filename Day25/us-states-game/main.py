import turtle

MAP_IMG = "blank_states_img.gif"

# Initialize variables
states_dictionary = {}
states_left = []
score = 0
game_on = True

# TODO: Read CSV

# TODO: Input CSV into states_dictionary & states_left

# Game screen setup
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(MAP_IMG)
turtle.shape(MAP_IMG)

answer_state = screen.textinput(title="Guess the State", prompt="What's the name of a US state?")

while game_on:
    # if answer_state is in states_left:
        # remove from states_left
        # print at location from states_dictionary
        # increase score, check if the game is done (50/50)
    # else:
    #     pass
    # text input answer state with score as title, end if 50/50
    pass


# Keep game screen open
turtle.mainloop()