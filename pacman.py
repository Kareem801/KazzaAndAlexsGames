
import turtle as t
import random
import time
def run():
    score = 0
    # window
    window = t.Screen()
    window.bgcolor("black")
    window.setup(800, 800)
    window.tracer(0)

    # display score
    t.color("white")
    t.penup()
    t.hideturtle()
    t.goto(0, 370)
    #t.write("Score: "+str(score), align=("center"), font=("Courier", 20))

    # player
    player = t.Turtle()
    player.shape("circle")
    player.color("yellow")
    player.shapesize(2, 2)
    player.penup()
    player.speed(0)

    foods = []
    for i in range(9):
        food = t.Turtle()
        food.speed(0)
        food.penup()
        food.color("white")
        food.shape("square")
        food.shapesize(0.5, 0.5)
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        food.setpos(x, y)
        foods.append(food)

    superFood = t.Turtle()
    superFood.speed(0)
    superFood.penup()
    superFood.color("#ffc42e")
    superFood.shape("square")
    superFood.shapesize(0.5, 0.5)
    x = random.randint(-370, 370)
    y = random.randint(-370, 370)
    superFood.setpos(x, y)

    eaten = 0

    # enemy1
    enemy1 = t.Turtle()
    enemy1.speed(0)
    enemy1.penup()
    colorPick = random.randint(1, 5)

    if colorPick == 1:
        enemy1.color("#2b80ff")
    elif colorPick == 2:
        enemy1.color("#ff1493")
    elif colorPick == 3:
        enemy1.color("#ff9e3d")
    elif colorPick == 4:
        enemy1.color("#ff0703")
    elif colorPick == 5:
        enemy1.color("#18ff1d")

    enemy1.shape("square")
    enemy1.shapesize(2, 2)
    x = random.randint(-380, 380)
    enemy1.setpos(x, 380)



    # enemy2
    enemy2 = t.Turtle()
    enemy2.speed(0)
    enemy2.penup()
    colorPick = random.randint(1, 5)

    if colorPick == 1:
        enemy2.color("#2b80ff")
    elif colorPick == 2:
        enemy2.color("#ff1493")
    elif colorPick == 3:
        enemy2.color("#ff9e3d")
    elif colorPick == 4:
        enemy2.color("#ff0703")
    elif colorPick == 5:
        enemy2.color("#18ff1d")

    enemy2.shape("square")
    enemy2.shapesize(2, 2)
    x = random.randint(-380, 380)
    enemy2.setpos(x, 380)

    # scoreT
    scoreT = t.Turtle()
    scoreT.penup()
    scoreT.hideturtle()
    scoreT.color("white")
    scoreT.goto(0, 370)

    scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))
    while True:
        # def movements
        def up():
            y = player.ycor()
            y += 15
            player.sety(y)
        def down():
            y = player.ycor()
            y -= 15
            player.sety(y)
        def left():
            x = player.xcor()
            x -= 15
            player.setx(x)
        def right():
            x = player.xcor()
            x += 15
            player.setx(x)

        # input movements
        window.listen()
        window.onkeypress(up, "w")
        window.onkeypress(down, "s")
        window.onkeypress(right, "d")
        window.onkeypress(left, "a")

        # border
        if player.xcor() > 350:
            player.setx(350)
        elif player.xcor() < -350:
            player.setx(-350)
        if player.ycor() > 350:
            player.sety(350)
        if player.ycor() < -350:
            player.sety(-350)
        
        
        
        # collision with food
        for food in foods:
            if player.distance(food) < 30:
                x = random.randint(-380, 380)
                y = random.randint(-380, 380)
                score += 50
                eaten += 1
                scoreT.clear()
                scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))
                food.setpos(x, y)
        
        if player.distance(superFood) < 30:
            score += 100
            eaten += 1
            scoreT.clear()
            scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))
            superFood.setpos(x, y)


        # enemy movement
        enemy1.setheading(enemy1.towards(player))

        enemy1.forward(0.5)
        enemy2.setheading(enemy2.towards(player))
        enemy2.forward(0.8)

        # collision with enemy
        if player.distance(enemy1) < 25 or player.distance(enemy2) < 25:
            t.hideturtle()
            t.color("white")
            t.goto(0, 0)
            t.clear()
            t.write("You died!", align="center", font=("Courier", 40))
            t.goto(0, 370)
            t.write("Score: "+str(score), align=("center"), font=("Courier", 20))
            break

        window.title(score)
        window.update()
    window.update()
    time.sleep(2)
    window.bye()
    t.done()