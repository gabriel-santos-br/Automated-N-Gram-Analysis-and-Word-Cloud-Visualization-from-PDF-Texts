import os
import csv
import pdfplumber
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams as nltk_ngrams
from collections import Counter

# Ensure that the necessary NLTK resources are downloaded
nltk.download('punkt', quiet=True)

# Define the base directory as the current directory of the script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths and directories
pdf_dir = os.path.join(base_dir, 'pdfs')  # Directory for PDF documents
csv_dir = os.path.join(base_dir, 'csv_results')  # Directory for CSV results

# Create the 'csv_results' directory if it doesn't exist
os.makedirs(csv_dir, exist_ok=True)

# Load stopwords from a file located in the 'stopwords' directory
stopwords_file = os.path.join(base_dir, 'stopwords', 'stopwords-en.txt')
with open(stopwords_file, 'r', encoding='utf-8') as file:
    stopwords = set(line.strip() for line in file)

# Define the n-grams to analyze (unigrams, bigrams, trigrams, and fourgrams)
n_range = range(1, 5)

def extract_text(pdf_file):
    """Extract text from a PDF file."""
    with pdfplumber.open(pdf_file) as pdf:
        return ' '.join(page.extract_text() or '' for page in pdf.pages)

def count_ngrams(text, n):
    """Count n-grams in a given text, excluding stopwords."""
    words = [word for word in word_tokenize(text.lower()) if word.isalpha() and word not in stopwords]
    return Counter(' '.join(gram) for gram in nltk_ngrams(words, n))

def save_to_csv(term_dict, csv_path, n):
    """Save the top n-grams to a CSV file."""
    top_terms = term_dict.most_common(20)
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, delimiter=';')
        csv_writer.writerow(['Term', 'Frequency'])
        csv_writer.writerows(top_terms)

# Process each PDF in the 'pdfs' directory and perform n-gram analysis
counters_analysis = {n: Counter() for n in n_range}
for file_name in os.listdir(pdf_dir):
    if file_name.endswith('.pdf'):
        text_content = extract_text(os.path.join(pdf_dir, file_name))
        for n in n_range:
            counters_analysis[n].update(count_ngrams(text_content, n))

# Save the top 20 n-grams to separate CSV files
for n in n_range:
    csv_file_path = os.path.join(csv_dir, f"results_{n}gram.csv")
    save_to_csv(counters_analysis[n], csv_file_path, n)

print("Analysis completed, and CSVs saved in", csv_dir)