import turtle
import random
import time

screen = turtle.Screen()
screen.title('Snake')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('turquoise')


turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()


score = 0
delay = 0.1


Sid = turtle.Turtle()
Sid.speed(0)
Sid.shape('square')
Sid.color('black')
Sid.penup()
Sid.goto(0, 0)
Sid.direction = 'stop'


fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

old_fruit = []


scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('black')
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align = "center", font = ("Courier", 24, "bold"))


def snake_go_up():
    if Sid.direction != "down":
        Sid.direction = "up"

def snake_go_down():
    if Sid.direction != "up":
        Sid.direction = "down"

def snake_go_left():
    if Sid.direction != "right":
        Sid.direction = "left"

def snake_go_right():
    if Sid.direction != "left":
        Sid.direction = "right"

def snake_move():
    if Sid.direction == "up":
        y = Sid.ycor()
        Sid.sety(y + 20)

    if Sid.direction == "down":
        y = Sid.ycor()
        Sid.sety(y - 20)

    if Sid.direction == "left":
        x = Sid.xcor()
        Sid.setx(x - 20)

    if Sid.direction == "right":
        x = Sid.xcor()
        Sid.setx(x + 20)

screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

while True:
    screen.update()

    if Sid.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x,y)
        scoring.clear()
        score = score + 1
        scoring.write("Score:{}".format(score), align =  "center",font = ("Courier", 24, "bold"))
        delay = delay - 0.001

        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    for index in range(len(old_fruit) - 1, 0,  -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = Sid.xcor()
        b = Sid.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    if Sid.xcor() > 280 or Sid.xcor() < -300 or Sid.ycor() > 240 or Sid.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0, 0)
        scoring.write("Game Over \n Your Score is {}".format(score), align ="center", font = ("Courier", 30, "bold"))

    for food in old_fruit:
        if food.distance(Sid) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write("Game Over \n Your Score is {}".format(score), align ="center", font = ("Courier", 30, "bold"))

    time.sleep(delay)
turtle.Terminator()


