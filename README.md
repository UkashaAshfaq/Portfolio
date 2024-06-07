# Traffic Sign Classification

This project is a Traffic Sign Classification model using a Convolutional Neural Network (CNN) built with TensorFlow and Keras. The model is trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset.

## Table of Contents

- [Installation](#installation)

- [Usage](#usage)

- [Project Structure](#project-structure)

- [Model Architecture](#model-architecture)

- [Dataset](#dataset)

- [Results](#results)

- [Contributing](#contributing)

- [License](#license)

## Installation

1. Clone the repository:

   ```bash

   git clone https://github.com/UkashaAshfaq/Portfolio.git
   cd Portfolio
   git checkout traffic

   ```

### Create a virtual environment and activate it:

python -m venv venv

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

### Install the required dependencies:

pip install -r requirements.txt

### Usage:

Ensure you have the GTSRB dataset downloaded and extracted into a directory. The directory should contain 43 subdirectories (from 0 to 42), each containing images in .ppm format.

### Run the training script:

python traffic.py path_to_dataset_directory [model.h5]

path_to_dataset_directory: Path to the directory containing the dataset.

[model.h5]: (Optional) Filename to save the trained model.

The script will train the model and optionally save it to the specified file.

Project Structure

traffic-sign-classification/

├── gtsrb/

│   ├── 0/

│   ├── 1/

│   ├── ...

│   └── 42/

│       └── *.ppm

├── traffic.py

├── requirements.txt

└── README.md

gtsrb/: Directory containing the dataset with subdirectories for each traffic sign category.

traffic.py: Script containing the main logic for training the model.

requirements.txt: List of dependencies required to run the project.

README.md: Project documentation.

### Model Architecture:

The model is a Convolutional Neural Network (CNN) with the following architecture:

Two convolutional layers with 64 filters each, followed by max-pooling layers.

A flatten layer to convert 2D feature maps to 1D feature vectors.

A dense hidden layer with 512 units and dropout for regularization.

An output layer with 43 units (one for each category) and softmax activation.

### Dataset:

The model is trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which contains images of 43 different types of traffic signs. The images are resized to 30x30 pixels and normalized to have pixel values between 0 and 1.

### Results:

After training for 10 epochs, the model achieves reasonable accuracy on the test set. The exact performance may vary based on training conditions and dataset variations.

### Contributing:

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License:

This project is licensed under the MIT License. See the LICENSE file for details.
