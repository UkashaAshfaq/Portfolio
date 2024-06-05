# Minesweeper Game with AI

This is a Python implementation of the classic Minesweeper game with an AI that can assist in making moves. The project includes a graphical user interface (GUI) using Pygame.

## Features

- Play the classic Minesweeper game.
- AI can make safe moves and random moves based on its knowledge base.
- Graphical interface using Pygame.
- Flag cells to mark suspected mines.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/UkashaAshfaq/Portfolio.git
    cd Portfolio
    git checkout minesweeper
    ```

2. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Download the assets:**
    
    Ensure you have the following folder structure:

   ```

     assets/

   ├── fonts/

    │── OpenSans-Regular.ttf

    └── images/

        ├── flag.png

        └── mine.png
    ```

## Usage

Run the game using the following command:

```sh
python runner.py
```

### Controls:

Left Click: Reveal a cell.

Right Click: Flag or unflag a cell as a mine.

AI Move Button: Let the AI make a move.

Reset Button: Start a new game.

### How it Works:

Minesweeper Class

Minesweeper: Represents the Minesweeper game.

__init__(height, width, mines): Initializes the game board.

print(): Prints a text-based representation of the board.

is_mine(cell): Checks if a cell is a mine.

nearby_mines(cell): Returns the number of mines around a cell.

won(): Checks if all mines have been flagged.

Sentence Class

Sentence: Represents a logical statement about the Minesweeper game.

known_mines(): Returns the set of all cells in the sentence known to be mines.

known_safes(): Returns the set of all cells in the sentence known to be safe.

mark_mine(cell): Updates the sentence given that a cell is a mine.

mark_safe(cell): Updates the sentence given that a cell is safe.

MinesweeperAI Class

MinesweeperAI: Represents the AI player for the Minesweeper game.

mark_mine(cell): Marks a cell as a mine.

mark_safe(cell): Marks a cell as safe.

add_knowledge(cell, count): Adds knowledge to the AI based on the revealed cell and number of nearby mines.

make_safe_move(): Returns a safe cell to choose.

make_random_move(): Returns a random move to make.

### Assets:

Fonts and images should be placed in the assets folder.

#### Fonts:

OpenSans-Regular.ttf should be located in assets/fonts/.

#### Images:

flag.png and mine.png should be located in assets/images/.

### Requirements:

Python 3.6+

Pygame
### Contributing:

Contributions are welcome! Please feel free to submit a Pull Request.

### License:

This project is licensed under the MIT License.
