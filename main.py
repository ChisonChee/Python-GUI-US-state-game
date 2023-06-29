import turtle
import pandas
import pandas as pd
from statespointer import StatesPointer
from scoretrack import ScoreTrack

HISTORY_DATA_FILE = "./score_records.csv"
STATES_DATA_FILE = "./50_states.csv"

score_track = ScoreTrack()
state = StatesPointer()
screen = turtle.Screen()
screen.title("U.S. STATES GAME")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

history_data = pd.read_csv(HISTORY_DATA_FILE)
state_list = history_data["Guessed state"].to_list()
x_cor_list = history_data["x_cor"].to_list()
y_cor_list = history_data["y_cor"].to_list()

if len(state_list) > 0:
    for state_num in range(len(state_list)):
        the_state = state_list[state_num]
        the_x_cor = x_cor_list[state_num]
        the_y_cor = y_cor_list[state_num]
        the_state_position = (the_x_cor, the_y_cor)
        state.coordinated(the_state, the_state_position)

while score_track.read_score_history() <= 50:
    state_is = screen.textinput(f"U.S. STATES. {score_track.read_score_history()}/50", "Please name U.S. State.").lower()
    state_title_case = state_is.replace(state_is[0], state_is[0].upper(), 1)
    state_is = state_title_case

    data = pandas.read_csv(STATES_DATA_FILE)
    state_list = data["state"].to_list()

    if state_is in state_list:
        states_coordinate = data[data["state"] == state_is]
        x_cor = int(states_coordinate["x"])
        y_cor = int(states_coordinate["y"])
        position = (x_cor, y_cor)
        state.coordinated(state_is, position)
        score_track.guessed_state_data(state_is, x_cor, y_cor)
    else:
        pass
turtle.mainloop()
