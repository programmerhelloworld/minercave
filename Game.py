'''
================================================================
Copyright (c) 2025 Francesco Maresca @programmerhelloworld

Miner Cave Alpha Version (0.03)

================================================================
'''
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.input_field import InputField
from perlin_noise import PerlinNoise
import pygame
import random
import json
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

# Audio setups
pygame.mixer.init()
channel_index = 0

# Game version
version = 0.03
 
def play_sound(sound, increase):
    global channel_index
    pygame.mixer.Channel(channel_index).play(pygame.mixer.Sound(sound))
    if increase:
        channel_index += 1

play_sound("miscellaneous/music.mp3", True)
# Initialize game
game = Ursina(
    title="Miner Cave",
    borderless=False,
    #size=(800, 600),
    vsync=False,
    use_ingame_console=False,
    fullscreen=False,
    fps=True
)


# Quick settings
development_mode = False

pauseText = Text("Game paused.\n Press F2 again to unpause it.", position=(-0.45, 0.1, 0), scale=3, #color = color.black, 
                 visible = False)

# Skyboxs
skybox = Sky(textures="miscellanoeus/sky.jpg")

# Game variables
block_textures = {
    "grass": load_texture("blocks/Grass.png"),
    "dirt": load_texture("blocks/Dirt.png"),
    "stone": load_texture("blocks/Stone.png"),
    "cobblestone": load_texture("blocks/Cobblestone.png"),
    "bricks": load_texture("blocks/Brick.png"),
    "sand": load_texture("blocks/Sand.png"),
    "roof": load_texture("blocks/Roof.png"),
    "glass": load_texture("blocks/Glass.png"),
    "wood": load_texture("blocks/Wood.png"),
    "water": load_texture("blocks/Water.png")
}

block_types = list(block_textures.keys())
selected_block_index = 0

# Perlin noise for terrain generation
noise = PerlinNoise(octaves=4, seed=random.randint(1, 100000000))
world_size = 20

# Save file path
SAVE_FILE = "world_save.minercavesave"

def save_world():
    app = QApplication(sys.argv)
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getSaveFileName(
        None,
        "Save World As",
        "",
        "Miner Cave Save Files (*.minercavesave)",
        options=options
    )
    
    if file_path:
        try:
            world_data = []
            for entity in scene.entities:
                if isinstance(entity, Block):
                    world_data.append({
                        "position": [entity.x, entity.y, entity.z],
                        "block_type": entity.block_type
                    })
            with open(file_path, "w") as f:
                json.dump(world_data, f, indent=4)
            print(f"World saved to {file_path}!")
        except Exception as e:
            print(f"Error saving world: {e}")

def getHeight():                                                        # Added this function in order to fix the falling glitch when loading world,                      
    for x in range(-world_size, world_size):                            # which gets a correct height where the player can spawn
        for z in range(-world_size, world_size):
            height = int(noise([x / 10, z / 10]) * 5)
    return height
plH = getHeight()

def generate_terrain():
    for x in range(-world_size, world_size):
        for z in range(-world_size, world_size):
            height = int(noise([x / 10, z / 10]) * 5)
            add_block((x, height, z), "grass")
            add_block((x, height-1, z), "dirt")
            add_block((x, height-2, z), "stone")
            
def load_world():
    app = QApplication(sys.argv)
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Open World Save File",
        "",
        "Miner Cave Save Files (*.minercavesave)",
        options=options
    )
    
    if file_path:
        try:
            for entity in scene.entities[:]:
                if isinstance(entity, Block):
                    destroy(entity)

            with open(file_path, "r") as f:
                world_data = json.load(f)
                for block_data in world_data:
                    position = tuple(block_data["position"])
                    block_type = block_data["block_type"]
                    add_block(position, block_type)
                player.position = (0, plH, 0)                           # If removed, when loading a new world collision will bug and player will fall
            print(f"World loaded from {file_path}!")
        except Exception as e:
            print(f"Error loading world: {e}")
                

def add_block(position, block_type):
    if block_type in block_textures:
        Block(position=position, block_type=block_type)

class Block(Entity):
    def __init__(self, position, block_type):
        super().__init__(
            position=position,
            model="cube",
            texture=block_textures.get(block_type),
            collider="box",
            scale=1,
            origin_y=-0.5
        )
        self.block_type = block_type

player = FirstPersonController(
    name = "Player",
    mouse_sensitivity=Vec2(100, 100),
    position=(0, plH+2, 0)                                              # Adding two blocks height in order to be sure that spawns on air and not inside blocks (colliding bug needs to be fixed ASAP)
)

# Mini block 
mini_block = Entity(
    parent=camera,
    model="cube",
    texture=block_textures[block_types[selected_block_index]],
    scale=0.2,
    position=(0.35, -0.25, 0.5),
    rotation=(-15, -30, -5),
)

def update():
    if time.time() % 0.1 < 0.05:
        pass


# Update of selected block -> mini block texture
def update_selected_block(index):
    global selected_block_index
    selected_block_index = index
    mini_block.texture = block_textures[block_types[selected_block_index]]

# Input keys
def input(key):
    global selected_block_index
    if key == 'u':
        save_world()
    elif key == 'g':
        player.position = (1, 12, 1)
        load_world()
    elif key == 'f2':                                                   # Basically freezes the game, thinking of including a real pause menu someday
        if (player.enabled == True):
            player.enabled = False
            pauseText.visible = True
        else:
            player.enabled = True
            pauseText.visible = False
    elif key == 'f3':
            pygame.mixer.stop
    elif key == 'right mouse down' and menu_mode == False:
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            add_block(hit_info.entity.position + hit_info.normal, block_types[selected_block_index])
    elif key == 'left mouse down' and mouse.hovered_entity and menu_mode == False:
        if hasattr(mouse.hovered_entity, 'block_type') and mouse.hovered_entity.block_type != "bedrock":
            destroy(mouse.hovered_entity)
            play_sound("miscellaneous/punch.mp3", False)
    elif key.isdigit() and 1 <= int(key) <= len(block_types):
        selected_block_index = int(key) - 1
        update_mini_block()

def update_mini_block():
    mini_block.texture = block_textures[block_types[selected_block_index]]

generate_terrain()


# ---------- Creating the menu interface ----------

playerName = InputField(max_lines=1, default_value=player.name, character_limit=15, active=True)

guiText1 = Text(f"Francesco Maresca's Miner Cave Alpha Version ({version})", position=(-0.65, 0.48), scale=1)


def update():
    if (player.y == plH-12):
        player.y = plH+2
        player.x -= 1
        player.y -= 1
menu_mode = True                                                        # Defines the state of the game
if menu_mode == True:
    logo = Sprite("miscellaneous/logo.png", parent=camera.ui, position=(0,0.25), scale = 0.07)
    logo.enabled = True
    player.enabled = False                                              # Player, when in the menu, not able to play
    playerName.enabled = True                                           # Shows the player inputField

def nameAuthentication():
    player.name = playerName.text
    print(f"Player name: {player.name}")



def setMenuMode():
    global menu_mode  # Use the global menu_mode variable
    nameAuthentication()
    logo.enabled = False
    guiText2 = Text("Player: " + player.name, position=(-0.65, 0.44), scale=1)
    def update_gui_text():
        guiText2.text = f"Player: {player.name}"
    menu_mode = False
    playerName.enabled = False
    print("Play")
    player.enabled = True                                               # Enable the player to start the game
    playButton.enabled = False                                          # Disable the play button after clicking
    player.position = (0, plH + 2, 0)                                   # Make sure the player starts in a valid position
    
    # Block bar
    bar_position = Vec3(0, -0.42, 0)
    block_bar = []
    num_blocks = len(block_types)
    bar_width = num_blocks * 0.12
    start_position_x = -bar_width / 2

    for i, block_type in enumerate(block_types):
        block_bar.append(Entity(
            parent=camera.ui,
            model="quad",
            texture=block_textures[block_type],
            scale=(0.1, 0.1),
            position=(start_position_x + (i * 0.12), bar_position.y),
            on_click=lambda i=i: update_selected_block(i)               # Fix closure by using i as a default argument
        ))


playButton = Button(
    parent = camera.ui,
    #model='rectangle',
    text_size = 2,
    position= (0, -0.25),
    scale = 0.30,
    text="Play Single Player!",
    texture= "blocks/Grass.png",
    #text_color = color.black,
    on_click = setMenuMode
)



game.run()
