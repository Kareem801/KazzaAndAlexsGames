
import turtle as t
import random
import time
from pathlib import Path
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
    t.register_shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanUp.gif")
    t.register_shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanDown.gif")
    t.register_shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanRight.gif")
    t.register_shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanLeft.gif")
    player.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanRight.gif")
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
    t.register_shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\cherry.gif")
    superFood.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\cherry.gif")
    x = random.randint(-370, 370)
    y = random.randint(-370, 370)
    superFood.setpos(x, y)

    eaten = 0

    # enemy1
    enemy1 = t.Turtle()
    enemy1.speed(5)
    enemy1.penup()
    t.register_shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\blueGhost.gif")
    enemy1.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\blueGhost.gif")
    x = random.randint(-380, 380)
    enemy1.setpos(x, 380)



    # enemy2
    enemy2 = t.Turtle()
    enemy2.speed(5)
    enemy2.penup()
    t.register_shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\redGhost.gif")
    enemy2.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\redGhost.gif")
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
            player.heading = "Up"
            player.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanUp.gif")
        
        def down():
            player.heading = "Down"
            player.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanDown.gif")

        def left():
            player.heading = "Left"
            player.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanLeft.gif")

        def right():
            player.heading = "Right"
            player.shape(str(Path().absolute())+"\\pacman\\pacmanSprites\\pacmanRight.gif")
        
        def move():
            if player.heading == "Up":
                player.sety(player.ycor()+2.5)
            if player.heading == "Down":
                player.sety(player.ycor()-2.5)
            if player.heading == "Left":
                player.setx(player.xcor()-2.5)
            if player.heading == "Right":
                player.setx(player.xcor()+2.5)

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
            if player.distance(food) < 35:
                x = random.randint(-380, 380)
                y = random.randint(-380, 380)
                score += 50
                eaten += 1
                scoreT.clear()
                scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))
                food.setpos(x, y)
        
        if player.distance(superFood) < 50:
            score += 100
            eaten += 1
            scoreT.clear()
            scoreT.write("Score: "+str(score), align=("center"), font=("Courier", 20))
            x = random.randint(-380, 380)
            y = random.randint(-380, 380)
            superFood.setpos(x, y)


        # enemy movement
        enemy1.setheading(enemy1.towards(player))

        enemy1.forward(0.2+(score/1000))
        enemy2.setheading(enemy2.towards(player))
        enemy2.forward(0.3+(score/1000))

        # collision with enemy
        if player.distance(enemy1) < 50 or player.distance(enemy2) < 50:
            t.hideturtle()
            t.color("white")
            t.goto(0, 0)
            t.clear()
            t.write("You died!", align="center", font=("Courier", 40))
            t.goto(0, 370)
            t.write("Score: "+str(score), align=("center"), font=("Courier", 20))
            break

        move()
        window.title(score)
        window.update()
    window.update()
    time.sleep(2)
    window.bye()
    t.done()