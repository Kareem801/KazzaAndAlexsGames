from importlib.resources import path
import turtle as t
from pathlib import Path

window = t.Screen()
window.setup(800, 800)
window.bgcolor("black")
window.tracer(0)

player = t.Turtle()
player.color("white")
player.speed(0)
t.register_shape(str(Path().absolute())+"\\asteroidsSprites\\spaceship.gif")
player.shape(str(Path().absolute())+"\\asteroidsSprites\\spaceship.gif")
while True:
    window.update()