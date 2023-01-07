import turtle

# Constants
ALIGN = "center"
FONT_CONFIG = ("Courier", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT_CONFIG)
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=ALIGN, font=FONT_CONFIG)
