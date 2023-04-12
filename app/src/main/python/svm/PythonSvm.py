import pandas as pd

# Import data
df = pd.read_csv('app/src/main/resources/listings.csv')

'''
THIS USES running frequency for dynamic labelling

# Label the data (1) (label running frequencies)
df['actual_frequency'] = 0

df['actual_frequency'] = df.groupby('neighbourhood').cumcount() + 1

df.to_csv('app/src/main/resources/updated_listings.csv', index=False)
'''

# Label the data (1) (label fixed frequencies)

df['actual_frequency'] = 0

df['actual_frequency'] = df.groupby('neighbourhood')['neighbourhood'].transform('count')


# Label the data (2) (label heavy hitters) - OBS this is a fixed dataset size for training

l1Norm = len(df['neighbourhood'])
epsilon = 0.01
threshold = l1Norm * epsilon

df['heavy_hitter'] = df['actual_frequency'].apply(lambda x: 'heavy' if x > threshold else 'not_heavy')

df.to_csv('app/src/main/resources/updated_listings.csv', index=False)

#print(threshold)

# SVM on labelled data

# Write predictions to CSV file 

