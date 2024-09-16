import turtle
import random
import math
import time
from enum import nonmember

score = 0
clicked_x = None
clicked_y = None

def on_click(x, y):
    global clicked_x, clicked_y
    clicked_x = x
    clicked_y = y

def ball_clicked(x, y):
    global score
    ball_x, ball_y = random_balls.position()
    ball_heading = random_balls.heading()
    ball_distance = 20


    distance_to_ball = math.sqrt((x - ball_x) ** 2 + (y - ball_y) ** 2)

    if distance_to_ball < ball_distance:
        score += 1
        turtle_instance.clear()
        turtle_instance.write(f"points: {score}", font=('Courier', 30, 'italic'), align="left")

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("The Catch")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")
turtle_instance.shape('circle')
turtle_instance.hideturtle()

random_balls = turtle.Turtle()
random_balls.color("green")
random_balls.shape("turtle")
random_balls.shapesize(2,2,2)

turtle_pen = turtle.Turtle()
turtle_pen.hideturtle()
turtle_pen.pendown()

random_balls.onclick(ball_clicked)

turtle_screen.onclick(on_click)

# Create a timer box
box = turtle.Turtle()
box.hideturtle()
box.color("black")
box.pensize(5)
box.penup()
box.setx(50)
box.sety(150)
box.pendown()
box.forward(250)
box.left(90)
box.forward(100)
box.left(90)
box.forward(250)
box.left(90)
box.forward(100)
box.left(90)
box.forward(150)
x = 0
t = int(turtle.textinput("CatchTheTurtle","Please enter time" ))





turtle_instance2 = turtle.Turtle()
turtle_instance2.color("black")
turtle_instance2.shape('circle')
turtle_instance2.hideturtle()
style = ('Courier', 30, 'italic')
turtle_instance2.penup()
turtle_instance2.goto(250, 175)

turtle_instance3 = turtle.Turtle()
turtle_instance3.color("black")
turtle_instance3.shape('circle')
turtle_instance3.hideturtle()
turtle_instance3.penup()
turtle_instance3.goto(195, 175)
turtle_instance3.write("Timer:", font=style, align="right")

turtle_instance.penup()
turtle_instance.goto(-250, 175)
turtle_instance.write(f"points: {score}", font=style, align="left")

while t >= 0:
    random_balls.teleport(random.randint(-175, 100), random.randint(-250, 150))
    time.sleep(1)
    turtle_instance2.clear()
    turtle_instance2.write(t, font=style, align="right")
    t -= 1


turtle_instance5 = turtle.Turtle()
turtle_instance5.color("black")
turtle_instance5.shape('circle')
turtle_instance5.hideturtle()

turtle_instance5.penup()
turtle_instance5.goto(35, 35)

if t == -1:

    turtle_instance5.write("Game Over! Your score is {}".format(score), font=style, align="center")

    turtle.mainloop()