from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level =1
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f"Level: {self.level} ", align="left",font= FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level} ", align="left", font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        