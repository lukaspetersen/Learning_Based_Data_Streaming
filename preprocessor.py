import sys
import time
import os
import csv
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# Setting nltk data environment variable
os.environ["NLTK_DATA"] = "/Users/lukaspetersen/.nltk_data"

def remove_backslashes(filename):
    """Function to remove backslashes from the file"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('\\', '')
    output_filename = f'output_{time.strftime("%Y%m%d-%H%M%S")}_nobackslashes.csv'
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"File with backslashes removed: {output_filename}")

def crop_csv(filename, X):
    """Function to crop the csv file"""
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = [next(reader) for _ in range(X)]
    cropped_filename = f'output_{time.strftime("%Y%m%d-%H%M%S")}_cropped.csv'
    with open(cropped_filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
    print(f"Cropped CSV file: {cropped_filename}")

def remove_stopwords(filename, column):
    """Function to remove stopwords"""
    stop_words = stopwords.words('english')
    added_stopwords = ["k", "cant", "got"]
    stop_words.extend(added_stopwords)
    data = pd.read_csv(filename, header=None)
    print("Removing stopwords...")
    data[column] = [' '.join([word.lower() for word in word_tokenize(row) if word.isalpha() and word.lower() not in stop_words]) for row in tqdm(data[column])]
    data.to_csv(f'output_{time.strftime("%Y%m%d-%H%M%S")}_nostopwords.csv', index=False)

def create_vector_representation(filename, column):
    data = pd.read_csv(filename, header=None)

    # Drop the rows where the column has null values
    data = data.dropna(subset=[column])

    # Convert the entire column to string type
    data[column] = data[column].astype(str)

    print("Creating vector representation...")
    sentences = [[word.lower() for word in word_tokenize(row) if word.isalpha()] for row in tqdm(data[column])]
    model = Word2Vec(sentences, min_count=1)
    vectors = {word: model.wv[word] for word in model.wv.index_to_key}
    output_filename = f'vectors_{time.strftime("%Y%m%d-%H%M%S")}.csv'
    pd.DataFrame.from_dict(vectors, orient='index').to_csv(output_filename)
    print(f"Vector representations saved to: {output_filename}")

def open_file():
    filename = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),("All Files","*.*")))
    return filename

def get_column():
    column = simpledialog.askinteger("Input", "Enter the column to be processed:")
    return column

def select_operation(root, operations):
    tkvar = tk.StringVar(root)
    popupMenu = tk.OptionMenu(root, tkvar, *operations)
    tk.Label(root, text="Choose an operation").grid(row=2, column=1)
    popupMenu.grid(row=3, column=1)
    
    # create a button that will store the selection and close the root window when pressed
    def submit():
        root.operation = tkvar.get()
        root.destroy()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=4, column=1)

def main():
    root = tk.Tk()

    # Center the window
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_top = int(root.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    root.geometry("+{}+{}".format(position_right, position_top))

    # Prevent window from being resizable
    # root.resizable(False, False)

    filename = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),("All Files","*.*")))
    tk.Label(root, text="Selected File: " + os.path.basename(filename)).grid(row=0, column=1)
    operations = ['REMOVE BACKSLASHES', 'CROP', 'REMOVE STOPWORDS', 'CREATE VECTOR REPRESENTATION']
    select_operation(root, operations)

    root.mainloop()

    operation = root.operation 

    if operation == 'crop':
        X = simpledialog.askinteger("Input", "Enter the number of rows to retain:")
        crop_csv(filename, X)
    elif operation == 'REMOVE BACKSLASHES':
        remove_backslashes(filename)
    elif operation in ['REMOVE STOPWORDS', 'CREATE VECTOR REPRESENTATION']:
        column = simpledialog.askinteger("Input", "Enter the COLUMN containing the information to be processed:")
        preprocessed = messagebox.askyesno("Question", "Has the file been preprocessed?")
        if not preprocessed:
            messagebox.showinfo("Information", "Please preprocess the file first.")
            return
        elif operation == 'REMOVE STOPWORDS':
            remove_stopwords(filename, column)
        elif operation == 'CREATE VECTOR REPRESENTATION':
            create_vector_representation(filename, column)

if __name__ == "__main__":
    main()