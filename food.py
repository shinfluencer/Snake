import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.refresh()

    def refresh(self):
        """Moves food to a random position."""
        
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
