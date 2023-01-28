import turtle as t
import random
import time
from mouse import *

def run():
    score = 0
    roundList = []

    window = t.Screen()
    window.tracer(0)
    window.bgcolor("black")
    window.setup(1000, 800)
    window.title("Atari")

    scoreT = t.Turtle()
    scoreT.hideturtle()
    scoreT.penup()
    scoreT.color("white")
    scoreT.speed(0)
    scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))


    paddle = t.Turtle()
    paddle.speed(0)
    paddle.penup()
    paddle.color("white")
    paddle.shape("square")
    paddle.shapesize(0.5, 7)
    paddle.goto(0, -320)


    def brickSet():
        bricks = []
        for i in range(12):
            brick = t.Turtle()
            brick.speed(0)
            brick.penup()
            brick.shape("square")
            brick.shapesize(1, 3.5)
            brick.color("red")
            if len(bricks) == 0:
                brick.goto(445, 340)
                bricks.append(brick)
            else:
                y = bricks[i-1].ycor()
                x = bricks[i-1].xcor() - 82
                brick.goto(x, y)
                bricks.append(brick)

        for i in range(12):
            brick = t.Turtle()
            brick.penup()
            brick.shape("square")
            brick.speed(0)
            brick.shapesize(1, 3.5)
            brick.color("orange")
            if len(bricks) == 12:
                brick.goto(445, 300)
                bricks.append(brick)
            else:
                y = bricks[(i+12)-1].ycor()
                x = bricks[(i+12)-1].xcor() - 82
                brick.goto(x, y)
                bricks.append(brick)

        for i in range(12):
            brick = t.Turtle()
            brick.penup()
            brick.shape("square")
            brick.speed(0)
            brick.shapesize(1, 3.5)
            brick.color("green")
            if len(bricks) == 24:
                brick.goto(445, 260)
                bricks.append(brick)
            else:
                y = bricks[(i+24)-1].ycor()
                x = bricks[(i+24)-1].xcor() - 82
                brick.goto(x, y)
                bricks.append(brick)

        for i in range(12):
            brick = t.Turtle()
            brick.penup()
            brick.shape("square")
            brick.speed(0)
            brick.shapesize(1, 3.5)
            brick.color("blue")
            if len(bricks) == 36:
                brick.goto(445, 220)
                bricks.append(brick)
            else:
                y = bricks[(i+36)-1].ycor()
                x = bricks[(i+36)-1].xcor() - 82
                brick.goto(x, y)
                bricks.append(brick)
        return (bricks)


    def reset():
        window.tracer(0)
        window.bgcolor("black")

        paddle = t.Turtle()
        paddle.speed(0)
        paddle.penup()
        paddle.color("white")
        paddle.shape("square")
        paddle.shapesize(0.5, 7)
        paddle.goto(0, -320)

        scoreT = t.Turtle()
        scoreT.hideturtle()
        scoreT.penup()
        scoreT.color("white")
        scoreT.speed(0)
        scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))

        ball = t.Turtle()
        ball.color("white")
        ball.penup()
        ball.shape("circle")
        ball.speed(0)
        ball.shapesize(2, 2)
        ball.setheading(random.randint(60, 100))

        bricks = brickSet()
        return (window, paddle, scoreT, ball, bricks)


    ball = t.Turtle()
    ball.color("white")
    ball.penup()
    ball.shape("circle")
    ball.speed(0)
    ball.shapesize(2, 2)
    ball.setheading(random.randint(60, 100))

    bricks = brickSet()
    while True:
        ball.forward(15+(len(roundList)*3))

        if ball.xcor() > 480 or ball.xcor() < -480:
            ball.setheading(((180 - ball.heading()) % 360) + random.randint(-15, 15))
        if ball.xcor() > 490:
            ball.setx(490)
        if ball.xcor() < -490:
            ball.setx(-490)
        if ball.ycor() > 380:
            ball.setheading((360 - ball.heading()) % 360)

        if ball.ycor()-25 <= paddle.ycor() <= ball.ycor()+25:
            if paddle.xcor() - 90 <= ball.xcor() <= paddle.xcor() + 90:
                ball.setheading(((360 - ball.heading()) % 360) + random.randint(-15, 15))
                ball.forward(20)

        if ball.ycor() < -380:
            t.color("white")
            t.hideturtle()
            t.clear()
            scoreT.clear()
            scoreT.goto(0, -30)
            t.write("You died!", align=("center"), font=("Courier", 50))
            scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))
            break


        for brick in bricks:
            if ball.distance(brick) < 40:
                ball.setheading(((360 - ball.heading()) %
                                360) + random.randint(-15, 15))
                brick.hideturtle()
                brick.goto(2000, 2000)
                score += 50

        x, y = get_position()
        x = x-540
        if x < 50:
            x = 50
        if x > 950:
            x = 950
        x = x - 500
        paddle.goto(x, paddle.ycor())

        scoreT.clear()
        scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))
        if ((score % 2400) == 0) and (score not in roundList):
            ball.goto(0, 0)
            ball.heading == "Stop"
            window.clear()
            roundList.append(score)
            window, paddle, scoreT, ball, bricks = reset()
        time.sleep(0.001)
        window.update()

    window.update()
    time.sleep(2)
    window.bye()
    t.done()