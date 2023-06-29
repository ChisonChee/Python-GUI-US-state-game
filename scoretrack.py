import pandas as pd
CSV_LOCATION = "./score_records.csv"


class ScoreTrack:
    def __init__(self):
        self.data = {
            "Guessed state": [],
            "x_cor": [],
            "y_cor": []
        }
        self.score = 0

    def guessed_state_data(self, state, x_cor, y_cor):
        self.data["Guessed state"].append(state)
        self.data["x_cor"].append(x_cor)
        self.data["y_cor"].append(y_cor)
        df = pd.DataFrame(self.data)
        if len(self.data["Guessed state"]) == 0 or len(self.data["Guessed state"]) ==50:
            df.to_csv(CSV_LOCATION, mode="w", index=False)
        elif 50>len(self.data["Guessed state"])>0:
            df.to_csv(CSV_LOCATION, mode="a", index=False, header= False)

    def read_score_history(self):
        data = pd.read_csv(CSV_LOCATION)
        guessed_state_list = data["Guessed state"].to_list()
        self.score = len(guessed_state_list)
        return self.score
