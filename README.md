# PageRank Algorithm

This repository contains an implementation of the PageRank algorithm.

PageRank is an algorithm used by Google Search to rank web pages in their search engine results.

It works by counting the number and quality of links to a page to determine a rough estimate of the website's importance.

## Project Structure

The repository contains the following files and directories:

- `pagerank.py`: The main script that contains the implementation of the PageRank algorithm.

- `corpus0`, `corpus1`, `corpus2`: Directories containing HTML files that represent different corpora for testing the PageRank algorithm.

## How to Use

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository to your local machine:

    ```bash

    git clone https://github.com/UkashaAshfaq/Portfolio.git
    cd Portfolio
    git checkout pagerank

    ```

3. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Running the PageRank Algorithm

To run the PageRank algorithm on a given corpus, use the following command:

```bash
python pagerank.py <corpus_directory>

```

Replace <corpus_directory> with the directory containing the HTML files (e.g., corpus0, corpus1, or corpus2).

### Example:

python pagerank.py corpus0

Explanation of the Script

crawl(directory): Parses a directory of HTML pages and returns a dictionary where each key is a page, and values are a list of all other pages in the corpus that are linked to by the page.

transition_model(corpus, page, damping_factor): Returns a probability distribution over which page to visit next, given a current page.

sample_pagerank(corpus, damping_factor, n): Returns PageRank values for each page by sampling n pages according to the transition model, starting with a page at random.

iterate_pagerank(corpus, damping_factor): Returns PageRank values for each page by iteratively updating PageRank values until convergence.

### Sample Output:

When you run the script, it will display the PageRank results obtained from sampling and iteration methods. Here's an example of the output:

```yaml

PageRank Results from Sampling (n = 10000)

  1.html: 0.1234

  2.html: 0.2345

  3.html: 0.3456

  4.html: 0.2965

PageRank Results from Iteration

  1.html: 0.1212

  2.html: 0.2323

  3.html: 0.3535

  4.html: 0.2930

```

### License:
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments:

This implementation is based on the PageRank algorithm originally developed by Larry Page and Sergey Brin.

### Contributing:

Contributions are welcome! Please fork the repository and submit a pull request for review.
