from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False,  align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", move=False,  align="center", font=("Arial", 24, "bold"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("blue")
    #     self.write("GAME OVER!!", align="center", font=("Courier", 66, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
