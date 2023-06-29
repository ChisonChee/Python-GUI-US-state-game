from turtle import Turtle


class StatesPointer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()

    def coordinated(self, state_name, position):
        self.setposition(position)
        self.write(state_name, False, align="center", font=("Courier", 8, "normal"))
