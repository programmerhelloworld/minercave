Miner Cave

Miner Cave is an immersive 3D sandbox game built using the Ursina Engine. Players can explore, build, and save their worlds while enjoying dynamic terrain generation and custom gameplay mechanics. This project is in its alpha stage and is a work in progress.

Features

Core Features

First-Person Exploration: Move through the world with an intuitive first-person controller.

Customizable Terrain: Dynamically generated terrain with Perlin noise, including caves, grasslands, and underground layers.

Block Interaction: Place and destroy blocks to modify your world in real time.

Skybox: A customizable skybox to enhance visual appeal.

Gameplay Features

Block Types: Multiple block types including grass, dirt, stone, cobblestone, and more.

Save and Load: Save your progress and reload worlds with the PyQt5 file dialog.

Custom HUD: A block selection bar and a preview mini-block HUD for an enhanced user experience.

Cave Generation: Procedurally generated caves with randomized layouts and block types.

Audio Integration: Background music and sound effects using PyGame.

Developer Mode

Adjustable camera clipping planes for testing.

Visual debugging aids, such as near and far rendering tweaks.

Requirements

Python Libraries

ursina

pygame

perlin_noise

PyQt5

numpy

noise

You can install the required libraries using pip:

pip install ursina pygame perlin-noise PyQt5 numpy noise

How to Run

Clone the repository:

git clone https://github.com/programmerhelloworld/minercave.git

Navigate to the project folder:

cd minercave

Run the main script:

python main.py

Controls

General Controls

Mouse: Look around

W/A/S/D: Move

Space: Jump

Shift: Sprint

Left Mouse Button: Destroy block

Right Mouse Button: Place block

Block Selection

1-9: Select block type

Click Block Icon: Select block from the bar

World Management

U: Save the world

G: Load a saved world

Developer Tools

Escape: Toggle cursor lock/unlock

File Structure

main.py: The main script to run the game.

blocks/: Folder containing textures for block types.

miscellaneous/: Folder containing audio files like background music.


Known Issues

Terrain generation can be slow for larger worlds.

Cave generation logic may produce overlapping layers.

File dialog (PyQt5) may interfere with certain OS window management.

Future Enhancements

Multiplayer support missing.

Advanced cave systems with biomes and minerals.

Better performance optimization for larger worlds.

Customizable block textures and modding support.

Acknowledgments

Special thanks to the open-source community for the libraries and tools that made this project possible.
