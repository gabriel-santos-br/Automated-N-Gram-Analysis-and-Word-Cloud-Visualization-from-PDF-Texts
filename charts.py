import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os


def create_word_cloud(csv_path, n_gram, prefer_horizontal=0.9):
    """
    Generate a word cloud from a CSV file containing n-gram frequency data.

    Parameters:
    - csv_path: Path to the directory where the CSV files are located.
    - n_gram: The specific n-gram for which to create the word cloud.
    - prefer_horizontal: The preference for horizontal word alignment in the word cloud.
    """
    # Construct the full path to the n-gram CSV file
    csv_file = os.path.join(csv_path, f'results_{n_gram}gram.csv')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, delimiter=';')

    # Convert the DataFrame to a dictionary with terms as keys and frequencies as values
    freq_dict = df.set_index('Term')['Frequency'].to_dict()

    # Set the path to save the word cloud images, relative to the script location
    script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
    image_path = os.path.join(script_dir, 'charts')  # Set the 'charts' directory relative to the script
    os.makedirs(image_path, exist_ok=True)  # Create the 'charts' directory if it does not exist

    # Create the word cloud object
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        prefer_horizontal=prefer_horizontal
    ).generate_from_frequencies(freq_dict)

    # Plot the word cloud
    plt.figure(figsize=(15, 7.5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('')

    # Save the word cloud image
    output_image_path = os.path.join(image_path, f'wordcloud_{n_gram}gram.png')
    plt.savefig(output_image_path, bbox_inches='tight')
    plt.show()


# Set the base path for CSV files relative to the script
base_csv_path = os.path.join(os.path.dirname(__file__), 'csv')

# Generate and display word clouds for 1-gram to 4-gram frequencies
for n_gram in ['1', '2', '3', '4']:
    create_word_cloud(base_csv_path, n_gram, prefer_horizontal=0.9)
