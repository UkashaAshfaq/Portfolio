# Nim Game with AI

This project implements the classic Nim game with an AI player that uses Q-learning to improve its performance over time. The game and AI are written in Python.

## Table of Contents

- [Description](#description)

- [Installation](#installation)

- [Usage](#usage)

- [Game Rules](#game-rules)

- [AI Training](#ai-training)

- [Contributing](#contributing)

- [License](#license)

## Description

The Nim game involves players taking turns to remove objects from heaps. The player forced to take the last object loses the game. This project includes:

- A `Nim` class representing the game state and rules.

- A `NimAI` class that implements Q-learning to allow the AI to play the game.

- A `train` function to train the AI by playing games against itself.

- A `play` function to play against the trained AI.

## Installation

1. Clone the repository:

    ```sh

    git clone https://github.com/UkashaAshfaq/Portfolio.git
    cd Portfolio
    git checkout nim

    ```

3. Ensure you have Python 3 installed. You can check your Python version with:

    ```sh

    python --version

    ```

4. (Optional) Create a virtual environment:

   ```sh

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    ```

5. Install any required dependencies (if any). For now, this project does not require any external libraries.

## Usage

To train the AI and play against it, run:

```sh

python play.py

```

The script will first train the AI by playing 10,000 games against itself. Then, it will allow you to play against the trained AI.


### Game Rules:

The game starts with a set of piles, each containing a certain number of objects.

Players take turns to remove one or more objects from a single pile.

The player forced to take the last object loses the game.

AI Training

The AI uses Q-learning to learn the best moves. The training process involves:

Simulating a number of games where the AI plays against itself.

Updating the Q-values for state-action pairs based on the outcomes of these games.

You can adjust the number of training games by changing the argument in the train function in play.py:

ai = train(10000)

### Contributing:

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

Fork the repository.

Create your feature branch: git checkout -b my-new-feature.

Commit your changes: git commit -am 'Add some feature'.

Push to the branch: git push origin my-new-feature.

Submit a pull request.

### License:

This project is licensed under the MIT License - see the LICENSE file for details.
