import turtle
import random
import time

score = 0
clicked_x = None
clicked_y = None
random_location = random.randint(-100, 100)

def on_click(x, y):
    global clicked_x, clicked_y
    clicked_x = x
    clicked_y = y

def ball_clicked(x, y):
    global score
    if (random_location - 20 <= x <= random_location + 20) and (random_location2 - 20 <= y <= random_location2 + 20):
        score += 1
        turtle_instance.clear()
        turtle_instance.write(f"Points: {score}", font=('Courier', 30, 'italic'), align="left")

# Setup screen
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("The Catch")

# Setup turtle instance for ball
random_balls = turtle.Turtle()
random_balls.color("green")
random_balls.shape("turtle")
random_balls.shapesize(2, 2, 2)

# Setup turtle instance for score display
turtle_instance = turtle.Turtle()
turtle_instance.hideturtle()
turtle_instance.penup()
turtle_instance.goto(-250, 175)
turtle_instance.write(f"Points: {score}", font=('Courier', 30, 'italic'), align="left")

# Setup turtle instance for timer
turtle_instance2 = turtle.Turtle()
turtle_instance2.hideturtle()
turtle_instance2.penup()
turtle_instance2.goto(250, 175)
style = ('Courier', 30, 'italic')

turtle_instance3 = turtle.Turtle()
turtle_instance3.hideturtle()
turtle_instance3.penup()
turtle_instance3.goto(195, 175)
turtle_instance3.write("Timer:", font=style, align="right")

# Draw timer box
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

# Setup click events
random_balls.onclick(ball_clicked)
turtle_screen.onclick(on_click)

# Timer input and game loop
t = int(input("Time:"))

start_time = time.time()
end_time = start_time + t

while time.time() < end_time:
    random_location = random.randint(-175, 100)
    random_location2 = random.randint(-250, 250)
    random_balls.goto(random_location, random_location2)

    # Update timer display
    remaining_time = int(end_time - time.time())
    turtle_instance2.clear()
    turtle_instance2.write(f"Timer: {remaining_time}", font=style, align="right")

    turtle_screen.update()
    time.sleep(1)

turtle.mainloop()
