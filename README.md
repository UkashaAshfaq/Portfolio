# BERT Masked Language Model and Attention Visualization

This project uses a pre-trained BERT model to predict masked tokens in a given text and visualize the self-attention scores across different layers and heads of the BERT model.

## Features

- **Masked Language Prediction:** Predict the top K tokens for a masked token in a given text.
- **Attention Visualization:** Generate graphical representations of self-attention scores for each attention head in each layer of the BERT model.

## Requirements

- Python 3.7 or higher
- TensorFlow
- Transformers (Hugging Face)
- PIL (Pillow)
- OpenSans font

## Installation

1. Clone this repository:
   
   git clone https://github.com/UkashaAshfaq/Portfolio/bert-attention-visualization.git
   cd bert-attention-visualization
   
2. Install the required packages:

pip install -r requirements.txt

## Usage:

Run the script:

python mask.py

Enter the text with a [MASK] token when prompted:

Example:

Text: The quick brown fox jumps over the [MASK] dog.
The script will output the top K predictions for the masked token and generate attention diagrams saved as PNG files in the current directory.

## Project Structure:

mask.py: The main script containing the core functionality.
assets/fonts/OpenSans-Regular.ttf: The font used for generating attention diagrams.
README.md: This file.
requirements.txt: List of required packages.

## Functions:

main()
The main function that orchestrates the tokenization, prediction, and visualization processes.

get_mask_token_index(mask_token_id, inputs)
Returns the index of the token with the specified mask_token_id in the inputs.

get_color_for_attention_score(attention_score)
Returns a shade of gray corresponding to the given attention_score.

visualize_attentions(tokens, attentions)
Produces graphical representations of self-attention scores for each attention head in each layer.

generate_diagram(layer_number, head_number, tokens, attention_weights)
Generates and saves a diagram representing self-attention scores for a single attention head.

## Contributing:

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License:

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements:

Hugging Face Transformers for the pre-trained BERT model.
TensorFlow for the deep learning framework.
Pillow for image processing.
