# Flappy Bird Game

This is a simple implementation of the Flappy Bird game using Python and Pygame.

## Description

This project is a basic Flappy Bird game where the player controls a bird, attempting to fly between green pipes without hitting them. Each time the bird passes through a pair of pipes, the score increases by one. If the bird hits a pipe, the game is over, and the player has the option to restart the game.

## Features

- Simple graphics and game mechanics
- Score tracking
- Restart functionality upon game over

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/flappy-bird-game.git
    ```
2. Navigate to the project directory:
    ```sh
    cd flappy-bird-game
    ```
3. Install the required dependencies:
    ```sh
    pip install pygame
    ```

## How to Run

1. Make sure you are in the project directory.
2. Run the game:
    ```sh
    python flappy_bird.py
    ```

## Controls

- Press `SPACE` to make the bird flap its wings.
- Press `R` to restart the game after a game over.

## Game Over

- If the bird hits a pipe, the game will display a "Game Over" message.
- Press `R` to restart the game and try again.

## Project Structure

flappy-bird-game/
│
├── bird.png
├── background.png
├── flappy_bird.py
└── README.md

- `flappy_bird.py`: The main game script.
- `bird.png`: The bird sprite image.
- `background.png`: The background image.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- This project was inspired by the popular Flappy Bird game.
- Thanks to the Pygame community for the excellent library and resources.

