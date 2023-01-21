import turtle as t
import time
import random
from playsound import playsound
from pathlib import Path
def run():
    score1 = 0
    score2 = 0

    t.speed(0)
    t.color("white")
    t.left(90)
    t.forward(400)
    t.back(800)
    t.penup()
    t.hideturtle()
    t.goto(0, -30)
    t.color("white")

    window = t.Screen()
    window.tracer(0)
    window.setup(1000, 800)
    window.bgcolor("black")
    window.title("Pong")

    scoreT = t.Turtle()
    scoreT.hideturtle()
    scoreT.penup()
    scoreT.color("white")
    scoreT.goto(0, 320)
    scoreT.write(str(score1)+"-"+str(score2), align="center", font=["impact", 50])


    paddle1 = t.Turtle()
    paddle1.penup()
    paddle1.shape("square")
    paddle1.shapesize(5,0.5)
    paddle1.color("red")
    paddle1.speed(0)
    paddle1.heading = "Stop"
    paddle1.goto(-450, 0)

    paddle2 = t.Turtle()
    paddle2.penup()
    paddle2.shape("square")
    paddle2.shapesize(5,0.5)
    paddle2.color("blue")
    paddle2.speed(0)
    paddle2.heading = "Stop"
    paddle2.goto(450, 0)

    ball = t.Turtle()
    ball.penup()
    ball.shape("circle")
    ball.shapesize(3, 3)
    ball.speed(0)
    ball.color("#b026ff")
    x = random.randint(120,240)
    ball.right(x)


    def up1():
        paddle1.heading = "Up"

    def down1():
        paddle1.heading = "Down"

    def up2():
        paddle2.heading = "Up"

    def down2():
        paddle2.heading = "Down"

    def move(user):
        if user.heading == "Up":
            user.sety(user.ycor()+10)
        elif user.heading == "Stop":
            user.sety(user.ycor())
        else:
            user.sety(user.ycor()-10)

    while True:
        window.listen()
        window.onkeypress(up1, "w")
        window.onkeypress(up2, "Up")
        window.onkeypress(down1, "s")
        window.onkeypress(down2, "Down")
        move(paddle1)
        move(paddle2)
        
        if paddle1.ycor() > 350:
            paddle1.sety(350)
        if paddle1.ycor() < -350:
            paddle1.sety(-350)
        if paddle2.ycor() > 350:
            paddle2.sety(350)
        if paddle2.ycor() < -350:
            paddle2.sety(-350)
        if ball.ycor() > 350:
            ball.sety(350)
        if ball.ycor() < -350:
            ball.sety(-350)
        
        
        ball.forward(10)

        if ball.xcor() > 480:
            score1 += 1
            scoreT.clear()
            scoreT.write(str(score1)+"-"+str(score2), align="center", font=["impact", 50])
            window.update()
            ball.goto(0,0)
            paddle1.heading = "Stop"
            paddle1.goto(-450, 0)
            paddle2.heading = "Stop"
            paddle2.goto(450, 0)
            time.sleep(1)
            ball.setheading(random.randint(120, 240))
        
        elif ball.xcor() < -480:
            score2 += 1
            scoreT.clear()
            scoreT.write(str(score1)+"-"+str(score2), align="center", font=["impact", 50])
            window.update()
            ball.goto(0,0)
            paddle1.heading = "Stop"
            paddle1.goto(-450, 0)
            paddle2.heading = "Stop"
            paddle2.goto(450, 0)
            time.sleep(1)
            ball.setheading(random.randint(120, 240))
            
        
        
        if abs(ball.ycor()) > 350 or abs(ball.ycor()) < -350:
            ball.setheading((360 - ball.heading()) % 360)
            
        
        if ball.xcor() <= -430:
            if paddle1.ycor() - 70 <= ball.ycor() <= paddle1.ycor() + 70:
                ball.setheading((180 - ball.heading()) % 360)
        
        if ball.xcor() >= 430:
            if paddle2.ycor() - 70 <= ball.ycor() <= paddle2.ycor() + 70:
                ball.setheading((180 - ball.heading()) % 360)
        
        time.sleep(0.009)
        
        if score1 == 7 or score2 == 7:
            ball.hideturtle()
            if score1 > score2:
                t.write("Red wins!", align="center", font=["impact", 100])
            else:
                t.write("Blue wins!", align="center", font=["impact", 100])
            break
        
        window.update()
    window.update()
    time.sleep(2)
    window.bye()
    t.done()