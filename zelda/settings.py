from pathlib import Path
WIDTH    = 1280 
HEIGHT   = 720
FPS      = 60
TILESIZE = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = str(Path().absolute())+"\\KazzaAndAlexsGames-main\\zelda\\graphics\\font\\joystix.ttf"
UI_FONT_SIZE = 18

# general colours
WATER_COLOUR = "#71ddee"
UI_BG_COLOUR = "#222222"
UI_BORDER_COLOUR = "#111111"
TEXT_COLOUR = "#EEEEEE"

# ui colours
HEALTH_COLOUR = "red"
ENERGY_COLOUR = "blue"
UI_BORDER_COLOUR_ACTIVE = "gold"

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15,'graphic':str(Path().absolute())+'/KazzaAndAlexsGames-main/zelda/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30,'graphic':str(Path().absolute())+'/KazzaAndAlexsGames-main/zelda/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':str(Path().absolute())+'/KazzaAndAlexsGames-main/zelda/graphics/weapons/axe/full.png'},
    'rapier':{'cooldown': 50, 'damage': 8, 'graphic':str(Path().absolute())+'/KazzaAndAlexsGames-main/zelda/graphics/weapons/rapier/full.png'},
    'sai':{'cooldown': 80, 'damage': 10, 'graphic':str(Path().absolute())+'/KazzaAndAlexsGames-main/zelda/graphics/weapons/sai/full.png'}}