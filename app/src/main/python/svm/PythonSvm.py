import pandas as pd

# Import data
df = pd.read_csv('app/src/main/resources/listings.csv')

# Label the data (1) (label running frequencies)
df['actual_frequency'] = 0

df['actual_frequency'] = df.groupby('neighbourhood').cumcount() + 1

df.to_csv('app/src/main/resources/updated_listings.csv', index=False)


# Label the data (2) (label heavy hitters)


# SVM on labelled data

# Write predictions to CSV file 

