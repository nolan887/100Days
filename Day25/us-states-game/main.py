import turtle
import pandas

MAP_IMG = "blank_states_img.gif"
ALIGNMENT = "left"
FONT = ("Menlo", 8, "normal")

# Initialize variables
score = 0
guesses = 1
game_on = True

# Custom
def print_state(statename):
    state_data = data[data.state == statename]
    # Because this is a row of data, you can tap directly into the row by column heading
    t.goto(int(state_data.x), int(state_data.y))
    t.write(statename, align=ALIGNMENT, font=FONT)
    t.goto(-75,225)

# Read CSV
data = pandas.read_csv("50_states.csv")
states_left = data.state.tolist()

# Game screen setup
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(MAP_IMG)
turtle.shape(MAP_IMG)
t = turtle.Turtle()
t.penup()
t.goto(-75, 225)

# First Question
answer_state = str.title(screen.textinput(title="Guess the State", prompt="What's the name of a US state?"))

# Begin game
while game_on:
    if answer_state == "Exit":
        break
    if answer_state in states_left:
        print(f"yup, {answer_state} is a state")
        states_left.remove(answer_state)
        score += 1
        print_state(answer_state)
        if score == 50:
            print("Game over, you win!")
            print(f"It took you {guesses} guesses.")
            game_on = False
    else:
        answer_state = str.title(
            screen.textinput(title=f"{score} / 50 States Correct", prompt="What's the name of a US state?"))
        guesses += 1

# Game is off from "break" above
missed_states = pandas.DataFrame(states_left)
missed_states.to_csv("states_to_learn.csv")

# Keep game screen open
turtle.mainloop()