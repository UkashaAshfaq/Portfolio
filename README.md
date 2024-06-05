# Heredity

This project simulates the inheritance of a genetic trait across multiple generations of a family. It calculates the probabilities of each family member having a specific gene and exhibiting a trait based on the provided data.

## Project Structure:

The project contains the following files:

- `heredity.py`: The main script that performs the probability calculations.

- `data/`: A directory containing CSV files with family data.

  - `family0.csv`

  - `family1.csv`

  - `family2.csv`

## How It Works

The script calculates the probability that each person in the family has 0, 1, or 2 copies of a particular gene and whether they exhibit a trait associated with that gene. It uses Bayesian inference to update these probabilities based on the known data and the inheritance rules.

## Dependencies:

This project requires Python 3.x. No additional libraries are required.

## Usage:

To run the script, navigate to the project directory and execute the following command:

```bash

python heredity.py data/family0.csv
Replace data/family0.csv with the appropriate file name (family1.csv or family2.csv) as needed.

```

### Example:

```bash
python heredity.py data/family1.csv
```

### Functions:

main()
The main function that orchestrates loading data, calculating probabilities, and printing results.

load_data(filename)
Loads gene and trait data from a CSV file into a dictionary.

powerset(s)
Returns a list of all possible subsets of a set s.

joint_probability(people, one_gene, two_genes, have_trait)
Computes and returns the joint probability of a specific genetic and trait configuration.

inherit_prob(parent_name, one_gene, two_genes)
Helper function for joint_probability that calculates the probability of a parent passing on a gene.

update(probabilities, one_gene, two_genes, have_trait, p)
Updates the probabilities dictionary with a new joint probability p.

normalize(probabilities)
Normalizes the probability distributions to ensure they sum to 1.

### Data Format:

The data files should be CSV files with the following columns:

name: The name of the person.
mother: The name of the person's mother.
father: The name of the person's father.
trait: 0 if the person does not have the trait, 1 if the person has the trait, or blank if unknown.

### Example:

name,mother,father,trait
Harry,,,
James,,,
Lily,,,
Contribution
If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.

### License:

This project is licensed under the MIT License.
