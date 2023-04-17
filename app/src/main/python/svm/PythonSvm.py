import pandas as pd

from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer


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

# We look at the accuracy in our paper

# word2vec and then features to scikit  

# dynamic threshold 









# SVM on labelled data

'''Based on neighbourhood and number of bed rooms'''

'''
# Encode the categorical variable "neighborhood" as numeric
label_encoder = LabelEncoder()
df["neighborhood_encoded"] = label_encoder.fit_transform(df["neighbourhood"])

# Select input features and target variable
X = df[["neighborhood_encoded", "neighbourhood_group"]]
y = df["heavy_hitter"]

# Impute missing values with the median of the non-missing values
imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(X)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create SVM classifier
clf = svm.SVC(kernel='linear')

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Predict the target variable on the testing data
y_pred = clf.predict(X_test)

# Add the predicted target variable to the original dataframe as a new column
df["predicted_is_heavy"] = clf.predict(df[["neighborhood_encoded", "neighbourhood_group"]])

# Write predictions to CSV file 
df.to_csv('app/src/main/resources/updated_listings.csv', index=False)
'''