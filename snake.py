import turtle as t
import time
import random
from pathlib import Path
def run():
    t.penup()
    t.speed(0)
    
    window = t.Screen()
    window.title("Snake")
    window.tracer(0)
    window.bgcolor("black")
    window.setup(800, 800)

    score = 0
    delay = 0.1

    head = t.Turtle()
    head.speed(0)
    head.shape("square")
    head.shapesize(1,1)
    head.color("#39ff14")
    head.penup()
    head.heading = ("stop")

    food = t.Turtle()
    food.speed(0)
    t.register_shape(str(Path().absolute())+"\\snakeSprites\\apple.gif")
    food.shape(str(Path().absolute())+"\\snakeSprites\\apple.gif")
    food.penup()
    food.color("#ff073a")
    food.goto(0, -100)



    segments = []

    def up():
        if head.heading != "down":
            head.heading = ("up")
    def down():
        if head.heading != "up":
            head.heading = ("down")
    def right():
        if head.heading != "left":
            head.heading = ("right")
    def left():
        if head.heading != "right":
            head.heading = ("left")

    def move():
        if head.heading == "up":
            y = head.ycor() + 20
            head.sety(y)
        if head.heading == "down":
            y = head.ycor() - 20
            head.sety(y)
        if head.heading == "right":
            x = head.xcor() + 20
            head.setx(x)
        if head.heading == "left":
            x = head.xcor() - 20
            head.setx(x)

    window.listen()
    window.onkeypress(up, "w")
    window.onkeypress(down, "s")
    window.onkeypress(left, "a")
    window.onkeypress(right, "d")

    while True:
        if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 390 or head.ycor() < -390:
            break

        if head.distance(food) < 35:
            x = random.randint(-380, 380)
            y = random.randint(-380, 380)
            food.goto(x, y)

            for i in range(3):
                newSegment = t.Turtle()
                newSegment.penup()
                newSegment.speed(0)
                newSegment.goto(1000, 1000)
                newSegment.shape("square")
                newSegment.color("#39ff14")
                newSegment.shapesize(1, 1)
                segments.append(newSegment)

            delay -= 0.001
            score += 50
        
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        
        move()
        
        for segment in segments:
            if segment.distance(head) < 10:
                t.hideturtle()
                t.color("white")
                t.goto(0, 0)
                t.clear()
                t.write("You died!", align="center", font=("Courier", 40))
                t.goto(0, -50)
                t.write("Score: "+str(score), align=("center"), font=("Courier", 20))
                window.update()
                time.sleep(2)
                window.bye()
                t.done()
        
        window.title(score)
        
        time.sleep(delay)
        
        window.update()
    
    
    t.hideturtle()
    t.color("white")
    t.goto(0, 0)
    t.clear()
    t.write("You died!", align="center", font=("Courier", 40))
    t.goto(0, -50)
    t.write("Score: "+str(score), align=("center"), font=("Courier", 20))
    
    window.update()
    time.sleep(2)
    window.bye()
    t.done()
