# Shopping Prediction with K-Nearest Neighbors

This project implements a K-Nearest Neighbors (KNN) model to predict whether a customer will generate revenue (purchase) based on their online shopping behavior. The model is trained and evaluated on a dataset containing various features about the user's browsing activity.

## Table of Contents

- [Overview](#overview)

- [Requirements](#requirements)

- [Usage](#usage)

- [Data Format](#data-format)

- [Functions](#functions)

- [Model Training and Evaluation](#model-training-and-evaluation)

- [Results](#results)

- [License](#license)

## Overview

This script uses the `scikit-learn` library to train a KNN classifier on online shopping data. The data includes features like the number of pages visited, duration spent on each page, and whether the visit occurred on a weekend, among others.

## Requirements

- `Python 3.x`
- `scikit-learn`
- `pandas`

You can install the required libraries using:

```sh

pip install scikit-learn pandas

```

### Usage:

To run the script, use the following command:

python shopping.py data/shopping.csv

Replace data/shopping.csv with the path to your CSV file containing the shopping data.

### Data Format:

The CSV file should contain the following columns:

Administrative: Integer

Administrative_Duration: Float

Informational: Integer

Informational_Duration: Float

ProductRelated: Integer

ProductRelated_Duration: Float

BounceRates: Float

ExitRates: Float

PageValues: Float

SpecialDay: Float

Month: String (e.g., "Jan", "Feb", "Mar", ...)

OperatingSystems: Integer

Browser: Integer

Region: Integer

TrafficType: Integer

VisitorType: String ("Returning_Visitor" or other)

Weekend: Boolean ("TRUE" or "FALSE")

Revenue: Boolean ("TRUE" or "FALSE")

Functions

main()

The main function that orchestrates the loading of data, training of the model, and evaluation of results.

load_data(filename)

Loads data from the given CSV file and returns two lists: evidence and labels.

train_model(evidence, labels)

Trains a KNN model with the given evidence and labels, and returns the trained model.

evaluate(labels, predictions)

Evaluates the model's predictions and returns the sensitivity (true positive rate) and specificity (true negative rate).

Model Training and Evaluation

The dataset is split into training and testing sets with a 60-40 ratio. The model is trained using the training set and evaluated on the testing set.

### Metrics:

Sensitivity (True Positive Rate): Proportion of actual positive labels that were accurately identified.

Specificity (True Negative Rate): Proportion of actual negative labels that were accurately identified.

### Results:

After running the script, the results will display:

The number of correct and incorrect predictions.

The True Positive Rate (Sensitivity).

The True Negative Rate (Specificity).

### Example output:

Correct: 105

Incorrect: 45

True Positive Rate: 78.95%

True Negative Rate: 65.00%

### License:

This project is licensed under the MIT License. See the LICENSE file for details.
