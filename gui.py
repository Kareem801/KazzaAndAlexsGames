
from tkinter import *
import pacman.pacman as pacman
import snake.snake as snake
import pong.pong as pong
import atari.atari as atari
import pyautogui
mainWindow = Tk()
width, height = pyautogui.size()
mainWindow.geometry(str(width)+"x"+str(height))
mainWindow.title("Kareem's Games")

mn = Menu(mainWindow) 
mainWindow.config(menu=mn)

pacmanButton = Button(mainWindow, text="Pacman", width=50, height=20, command=lambda: pacman.run())
snakeButton = Button(mainWindow, text="Snake", width=50, height=20, command=lambda: snake.run())
pongButton = Button(mainWindow, text="Pong", width=50, height=20, command=lambda: pong.run())
atariButton = Button(mainWindow, text="Atari", width=50, height=20, command=lambda: atari.run())

def buttonClear():
    pacmanButton.forget()
    snakeButton.forget()
    pongButton.forget()
    atariButton.forget()

def pacmanGame():
    buttonClear()
    pacmanButton.pack()

def snakeGame():
    buttonClear()
    snakeButton.pack()

def pongGame():
    buttonClear()
    pongButton.pack()

def atariGame():
    buttonClear()
    atariButton.pack()


gameMenu = Menu(mn)
mn.add_cascade(label='Games', menu=gameMenu)
gameMenu.add_command(label="Pacman", command=pacmanGame)
gameMenu.add_command(label="Snake", command=snakeGame)
gameMenu.add_command(label="Pong", command=pongGame)
gameMenu.add_command(label="Atari", command=atariGame)


mainWindow.mainloop()
