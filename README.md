# Sentence Parser

This project contains a simple sentence parser implemented using NLTK. The parser can process sentences, identify their grammatical structure, and extract noun phrase chunks.

## Files

- `parser.py`: The main script for parsing sentences.

- `requirements.txt`: List of dependencies required to run the project.

- `sentences/`: Directory containing example text files with sentences to be parsed.

## Setup

1. **Clone the repository**:

    ```sh

    git clone https://github.com/UkashaAshfaq/Portfolio.git

    cd Portfolio

    git checkout parser

    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh

    python -m venv venv

    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    ```

3. **Install dependencies**:

    ```sh

    pip install -r requirements.txt

    ```

4. **Download NLTK data**:

    The necessary NLTK data is automatically downloaded when you run `parser.py`.

## Usage

To parse a sentence, you can either provide a filename containing the sentence or input the sentence directly. Here are examples of both methods:

1. **Parse a sentence from a file**:

    ```sh

    python parser.py sentences/1.txt

    ```

2. **Input a sentence manually**:

    ```sh

    python parser.py

    ```

    You will be prompted to enter a sentence.

## Example Sentences

The `sentences` directory contains example sentences in text files named `1.txt`, `2.txt`, etc. Here are their contents:

1. `1.txt`: Holmes sat.

2. `2.txt`: Holmes lit a pipe.

3. `3.txt`: We arrived the day before Thursday.

4. `4.txt`: Holmes sat in the red armchair and he chuckled.

5. `5.txt`: My companion smiled an enigmatical smile.

6. `6.txt`: Holmes chuckled to himself.

7. `7.txt`: She never said a word until we were at the door here.

8. `8.txt`: Holmes sat down and lit his pipe.

9. `9.txt`: I had a country walk on Thursday and came home in a dreadful mess.

10. `10.txt`: I had a little moist red paint in the palm of my hand.

## Functions

### `preprocess(sentence)`

Converts a sentence to a list of words by:

- Converting all characters to lowercase.

- Removing any word that does not contain at least one alphabetic character.

### `np_chunk(tree)`

Returns a list of all noun phrase chunks in the sentence tree. A noun phrase chunk is defined as any subtree of the sentence whose label is "NP" that does not itself contain any other noun phrases as subtrees.

## Example Output

For the input sentence "Holmes sat in the red armchair and he chuckled.", the output will be:

(S

(NP Holmes)

(VP

(VP (V sat) (PP (P in) (NP (Det the) (Adj red) (N armchair))))

(Conj and)

(NP (N he))

(VP (V chuckled))))

Noun Phrase Chunks

Holmes

the red armchair

he

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

This project uses the NLTK library for natural language processing. For more information, visit [NLTK](https://www.nltk.org/).
