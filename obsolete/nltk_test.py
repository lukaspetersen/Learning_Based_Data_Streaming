import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import pandas as pd

filename = 'twitterdata.csv'

stop_words = nltk.corpus.stopwords.words('english')
added_stopwords = ["k", "cant", "got"]
stop_words.extend(added_stopwords)


with open(filename, 'rb') as f:
    # Try different encodings until the file can be decoded successfully
    for encoding in ['utf-8', 'latin-1', 'cp1252']:
        try:
            # Specify the delimiter used in the file (e.g., comma)
            test = pd.read_csv(f, encoding=encoding, delimiter=',', names=['V1', 'V2', 'V3', 'V4', 'V5', 'V6'])
            break
        except UnicodeDecodeError:
            pass
        except pd.errors.ParserError:
            # If the number of columns is incorrect, try a different delimiter (e.g., semicolon)
            f.seek(0)
            try:
                test = pd.read_csv(f, encoding=encoding, delimiter=';', names=['V1', 'V2', 'V3', 'V4', 'V5', 'V6'])
                break
            except pd.errors.ParserError:
                # If still incorrect, print an error message and exit the loop
                print(f"Error: Could not parse file {filename}")
                break



output = []

for index, row in test['V6'].iteritems():
    try:
        tokens = word_tokenize(row)
        filtered_row = [w.lower() for w in tokens if w.isalpha() and not w.lower() in stop_words]
        output.append({'index': index, 'words': filtered_row})
        print(filtered_row)
        print(index)
    except TypeError:
        print(f"Error: Could not tokenize row {index}")
        pass

outputdf = pd.DataFrame(output)
outputdf.to_csv('outputdf.csv', index=False)
