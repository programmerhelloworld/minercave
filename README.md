# Francesco Maresca's Miner Cave

Miner Cave is an immersive 3D sandbox game built using the **Ursina Engine**. Players can explore, build, and save their worlds while enjoying dynamic terrain generation and custom gameplay mechanics. This project is in its alpha stage and is a work in progress.

| ![Miner Cave Screenshot](https://github.com/user-attachments/assets/1127ee88-1e82-4b69-a0e5-5900d3e9fa88) | ![Miner Cave Logo](https://github.com/user-attachments/assets/2c813844-00ef-425d-a2dd-81f5801fb44c) |
|:--:|:--:|


## Features

### Core Features
- **Main menu with username insertion**: Starting from Alpha 0.03, Game comes with a menu where you can choose your username.
- **First-Person Exploration**: Move through the world with an intuitive first-person controller.
- **Customizable Terrain**: Dynamically generated terrain with Perlin noise, including caves, grasslands, and underground layers.
- **Block Interaction**: Place and destroy blocks to modify your world in real-time.
- **Skybox**: A customizable skybox to enhance visual appeal.

### Gameplay Features
- **Block Types**: Multiple block types including grass, dirt, stone, cobblestone, and more.
- **Save and Load**: Save your progress and reload worlds with the PyQt5 file dialog.
- **Custom HUD**: A block selection bar and a preview mini-block HUD for an enhanced user experience.
- **Cave Generation**: Procedurally generated caves with randomized layouts and block types.
- **Audio Integration**: Background music and sound effects using PyGame.

### Developer Mode
- Adjustable camera clipping planes for testing.
- Visual debugging aids, such as near and far rendering tweaks.

## Requirements

### Python Libraries
- `ursina`
- `pygame`
- `perlin-noise`
- `PyQt5`
- `numpy`
- `noise`

# MinerCave Game Instructions

## Installation

To run **MinerCave**, you need to install the required libraries. Use the following `pip` command:

```bash
pip install ursina pygame perlin-noise PyQt5 numpy noise
```

## Controls

### General Controls
- **Mouse**: Look around
- **W/A/S/D**: Move
- **Space**: Jump
- **Shift**: Sprint
- **Left Mouse Button**: Destroy block
- **Right Mouse Button**: Place block

### Block Selection
- **1-9**: Select block type
- **Click Block Icon**: Select block from the bar

### World Management
- **U**: Save the world
- **G**: Load a saved world

### Useful keys
- **F2**: Toggle cursor lock/unlock

## File Structure
- `Game.py`: The main script to run the game.
- `blocks/`: Folder containing textures for block types.
- `miscellaneous/`: Folder containing audio files like background music.

## Known Issues
- Terrain generation can be slow for larger worlds.
- Cave generation logic may produce overlapping layers.
- File dialog (PyQt5) may interfere with certain OS window management.

## Future Enhancements
- Multiplayer support.
- Advanced cave systems with biomes and minerals.
- Better performance optimization for larger worlds.
- Customizable block textures and modding support.

