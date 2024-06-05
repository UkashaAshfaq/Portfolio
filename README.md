# Crossword Puzzle Generator

This project is a Crossword Puzzle Generator that uses Constraint Satisfaction Problems (CSP) to fill in a crossword puzzle structure with a given set of words.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Generate crossword puzzles based on a predefined structure and word list.
- Use Constraint Satisfaction Problems (CSP) techniques including backtracking and arc-consistency.
- Output the filled crossword puzzle to the terminal or save it as an image.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/UkashaAshfaq/Portfolio.git
    cd Portfolio
    git checkout crossword
    ```

2. Navigate to the project directory:

    ```bash
    cd crossword
    ```

3. Install the required Python packages:

    Ensure you have the `Pillow` library installed, which is used for saving the crossword as an image.

## Usage

To generate a crossword puzzle, run the following command:

```bash
python generate.py data/structure1.txt data/words1.txt True output.png
```
data/structure1.txt is the path to the structure file.

data/words1.txt is the path to the words file.

True or False specifies whether to use interleaved arc-consistency with backtracking.

output.png is the optional path to save the generated crossword as an image.

## Project Structure:

kotlin

crossword-generator/

├── assets/

│── fonts/

│── OpenSans-Regular.ttf

├──data/

│── structure1.txt

│── structure2.txt

│── structure3.txt

│── words1.txt

│── words2.txt

│── words3.txt

├── crossword.py

├── generate.py

├── requirements.txt

└── README.md

assets/fonts/: Directory containing the font used for image output.

data/: Directory containing structure and words files.

crossword.py: Contains the Variable and Crossword classes which define the crossword structure and variables.

generate.py: Contains the CrosswordCreator class which handles the CSP logic and generates the crossword puzzle.

## License:

This project is licensed under the MIT License. See the LICENSE file for more details.
