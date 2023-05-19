import sys
import time
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import gensim
from gensim.models import Word2Vec
from tqdm import tqdm #PROGRESS BAR

import os
os.environ["NLTK_DATA"] = "/Users/lukaspetersen/.nltk_data"

def clean(row):
    if isinstance(row, str):
        # discard the row if it contains repeating quotes
        if re.search(r'"["]+', row):
            return None
        else:
            return re.sub('[^A-Za-z0-9 ]+', '', row)
    else:
        return None

def remove_stopwords(filename, column):
    stop_words = nltk.corpus.stopwords.words('english')
    added_stopwords = ["k", "cant", "got"]
    stop_words.extend(added_stopwords)
    data = pd.read_csv(filename, header=None)
    data = data[data[column].apply(clean).notnull()]
    print("Removing stopwords...")
    data[column] = [ ' '.join([word.lower() for word in word_tokenize(row) if word.isalpha() and not word.lower() in stop_words]) for row in tqdm(data[column])]
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    data.to_csv(f'output_stopwords_removed_{timestamp}.csv', index=False)

def create_vector_representation(filename, column):
    data = pd.read_csv(filename, header=None)
    data = data[data[column].apply(clean).notnull()]
    print("Creating vector representation...")
    sentences = [ [word.lower() for word in word_tokenize(row) if word.isalpha()] for row in tqdm(data[column])]
    model = Word2Vec(sentences, min_count=1)
    vectors = {word: model.wv[word] for word in model.wv.index_to_key}
    pd.DataFrame.from_dict(vectors, orient='index').to_csv(f'output_vector_representation_{time.strftime("%Y%m%d-%H%M%S")}.csv')

def main():
    filename = sys.argv[1]
    column = int(sys.argv[2])
    operation = sys.argv[3]

    if operation == 'remove stopwords':
        remove_stopwords(filename, column)
    elif operation == 'create vector representation':
        create_vector_representation(filename, column)
    else:
        print(f"Error: Unknown operation {operation}")

if __name__ == "__main__":
    main()
