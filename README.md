Automated N-Gram Analysis and Word Cloud Visualization from PDF Texts

PROJECT OVERVIEW
This project provides tools for extracting n-grams from PDF documents and creating visual word clouds from these terms. It is designed to assist in the bibliographic analysis of documents by visualizing the frequency of terms.

The `ngrams.py` script processes PDF documents to identify and count n-grams, filtering out common stopwords. The `charts.py` script then takes the resulting CSV files with n-gram frequency data and generates word cloud images.

GETTING STARTED
Prerequisites:
- Python 3.x
- Libraries required: pandas, matplotlib, wordcloud, nltk, pdfplumber

Installation:
1. Clone the repository to your machine.
2. Set up and activate the Python virtual environment.
3. Install the required Python libraries using the provided requirements.txt file.

Usage:
Run `ngrams.py` to analyze the PDFs and generate CSV files with n-gram data.
Run `charts.py` to create word cloud images from the CSV files.

PROJECT STRUCTURE
- .venv/                  Virtual environment for the project.
- charts/                 Directory to store generated word cloud images.
- csv/                    Directory to store CSV files with n-gram frequency data.
- pdf/                    Directory containing PDF documents to be analyzed.
- stopwords/              Directory containing lists of stopwords.
- requirements.txt        Contains all the dependencies for the project.
- README.txt              The file you are currently reading.
- ngrams.py               Script to filter n-grams on PDF documents.
- charts.py               Script to create charts with CSV n-grams.

CONTRIBUTING
Contributions are welcome. Please fork the repository, make your changes, and submit a pull request for review.

ACKNOWLEDGMENTS
We would like to thank all contributors and users for their interest in this project.

CONTACT
If you have any questions or feedback, please contact gabriel.santos.business.br@gmail.com
