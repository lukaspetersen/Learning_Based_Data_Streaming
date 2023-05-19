import sys
import time
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import gensim
from gensim.models import Word2Vec
from tqdm import tqdm
import csv


import os
os.environ["NLTK_DATA"] = "/Users/lukaspetersen/.nltk_data"


def clean(row):
    # Clean the text in a row
    if isinstance(row, str):
        if re.search(r'"["]+', row):
            return None  # Discard rows with repeating quotes
        else:
            return re.sub('[^A-Za-z0-9 ]+', '', row)  # Discard special characters
    else:
        return None

def remove_stopwords(filename, column):
    # Remove stopwords from a column in a CSV file
    stop_words = nltk.corpus.stopwords.words('english')
    added_stopwords = ["k", "cant", "got"]
    stop_words.extend(added_stopwords)  # Add custom stopwords
    data = pd.read_csv(filename, header=None)
    data = data[data[column].apply(clean).notnull()]  # Apply cleaning
    print("Removing stopwords...")
    data[column] = [ ' '.join([word.lower() for word in word_tokenize(row) if word.isalpha() and not word.lower() in stop_words]) for row in tqdm(data[column])]
    timestamp = time.strftime("%Y%m%d%H%M%S")
    data.to_csv(f'out_rmstop_{timestamp}.csv', index=False)

def create_vector_representation(filename, column):
    # Create word2vec representation for a column in a CSV file
    data = pd.read_csv(filename, header=None)
    data = data[data[column].apply(clean).notnull()]  # Apply cleaning
    print("Creating vector representation...")
    sentences = [ [word.lower() for word in word_tokenize(row) if word.isalpha()] for row in tqdm(data[column])]
    model = Word2Vec(sentences, min_count=1)
    vectors = {word: model.wv[word] for word in model.wv.index_to_key}
    timestamp = time.strftime("%Y%m%d%H%M%S")
    pd.DataFrame.from_dict(vectors, orient='index').to_csv(f'out_vec_{timestamp}.csv')

def crop_csv(filename, X):
    # Crop a CSV file to contain only the first X rows
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = [next(reader) for _ in range(X)]  # Read only X rows

    cropped_filename = f'crop_{X}_{filename}'
    with open(cropped_filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)

    print(f"Cropped CSV saved as: {cropped_filename}")

def remove_backslashes(filename):
    # Remove backslashes from a CSV file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.replace('\\', '')  # Remove backslashes
    timestamp = time.strftime("%Y%m%d%H%M%S")
    output_filename = f'out_rmbs_{timestamp}.csv'
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Output saved as: {output_filename}")

def get_csv_files():
    # Return a list of CSV files in the current directory
    files = os.listdir()
    return [file for file in files if file.endswith('.csv')]

def main():
    # Get a list of CSV files in the current directory
    csv_files = get_csv_files()

    # Print the CSV files and let the user select one
    for i, filename in enumerate(csv_files):
        print(f"{i + 1}. {filename}")
    file_choice = int(input("Enter the number of the CSV file: ")) - 1
    filename = csv_files[file_choice]

    # Ask the user to enter the column to be processed
    column = int(input("Enter number of column to be processed (index 0):")) 

    # Present the operations for the user to select
    operations = ['remove backslashes', 'crop', 'remove stopwords', 'create vector representation']
    for i, operation in enumerate(operations):
        print(f"{i + 1}. {operation}")
    operation_choice = int(input("Enter the number of the operation: ")) - 1
    operation = operations[operation_choice]

    # If crop operation selected, ask for number of rows
    if operation == 'crop':
        X = int(input("Enter the number of rows to retain: "))
        crop_csv(filename, X)
    else:
        # If operation is either 'remove stopwords' or 'create vector representation', check for preprocessing
        if operation in ['remove stopwords', 'create vector representation']:
            preprocessed = input("Has the file been preprocessed? (y/n): ")
            if preprocessed.lower() == 'n':
                print("Please preprocess the file first.")
                return

        if operation == 'remove backslashes':
            remove_backslashes(filename)
        elif operation == 'remove stopwords':
            remove_stopwords(filename, column)
        elif operation == 'create vector representation':
            create_vector_representation(filename, column)

if __name__ == "__main__":
    main()