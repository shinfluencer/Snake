import turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        
    def create_snake(self):
        """Creates a new snake at the start."""
        
        for position in STARTING_POSITIONS:
            self.add_part(position)
        
    def add_part(self, position):
        """Creates a new snake part and adds it to the parts list.

        Args:
            position (Tuple): The position of the new snake part.
        """
        
        new_part = turtle.Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(x=position[0], y=position[1])
        self.parts.append(new_part)

    def extend(self):
        """Adds a new part to the snake when it eats food."""
        
        new_position = (self.parts[len(self.parts) - 1].xcor() - 20, self.parts[len(self.parts) - 1].ycor() - 20)
        self.add_part(new_position)
        
    def move(self):
        """Moves the snake's body."""
        
        for part_n in range(len(self.parts) - 1, 0, -1):
            self.parts[part_n].goto(self.parts[part_n - 1].xcor(), self.parts[part_n - 1].ycor())
        
        self.head.forward(MOVE_DISTANCE)
        
    def go_up(self):
        """Makes the snake move upwards."""
        
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        """Makes the snake move downwards."""
        
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def go_left(self):
        """Makes the snake move left."""
        
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def go_right(self):
        """Makes the snake move right."""
        
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
