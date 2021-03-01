import turtle
import pandas as pd
from state import State

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

csv_name = "50_states.csv"
states = pd.read_csv(csv_name)

total = len(states.state)
answers = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(
        title=f"{answers}/{total} - Guess the state",
        prompt="What's amother state's name?: ",
    )
    if answer_state.capitalize() in states.state.values:
        state = states[states.state == answer_state.capitalize()]
        state_obj = State(state.state.values[0], (state.x.values[0], state.y.values[0]))
        answers += 1

    if answers == total:
        game_is_on = False
        print("You win")


turtle.mainloop()