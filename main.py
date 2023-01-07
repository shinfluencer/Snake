import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Window Setup
window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake")
window.tracer(0)

# Game Components
snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.listen()
window.onkey(key="Up", fun=snake.go_up)
window.onkey(key="Down", fun=snake.go_down)
window.onkey(key="Left", fun=snake.go_left)
window.onkey(key="Right", fun=snake.go_right)

playing = True

while playing:
    time.sleep(0.1)
    window.update()
    
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 270 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -270:
        scoreboard.game_over()
        playing = False
        
    for part in snake.parts:
        if part != snake.head:
            if snake.head.distance(part) < 10:
                scoreboard.game_over()
                playing = False
    
    snake.move()

window.mainloop()
