from tkinter import *
import pacman
import snake
import pyautogui
mainWindow = Tk()
width, height = pyautogui.size()
mainWindow.geometry(str(width)+"x"+str(height))
mainWindow.title("Kareem's Games")

mn = Menu(mainWindow) 
mainWindow.config(menu=mn)

pacmanButton = Button(mainWindow, text="Pacman", width=50, height=20, command=lambda: pacman.run())
snakeButton = Button(mainWindow, text="Snake", width=50, height=20, command=lambda: snake.run())

def buttonClear():
    pacmanButton.forget()
    snakeButton.forget()

def pacmanGame():
    buttonClear()
    pacmanButton.pack()

def snakeGame():
    buttonClear()
    snakeButton.pack()



gameMenu = Menu(mn)
mn.add_cascade(label='Games', menu=gameMenu)
gameMenu.add_command(label="Pacman", command=pacmanGame)
gameMenu.add_command(label="Snake", command=snakeGame)


mainWindow.mainloop()
