# boing backup
import playsound
from pathlib import Path



boing = ("/"+str(Path().absolute())+'/boing.mp3')
boing = boing.replace("\\", "/", -1)
print (boing)
playsound(boing)