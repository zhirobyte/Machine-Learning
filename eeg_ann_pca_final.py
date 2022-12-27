# -*- coding: utf-8 -*-
"""EEG ANN PCA- final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lIh0Vhkv9nLqXJC8eeYeSWFBXMLAK3El
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# Load the EEG data and labels from a CSV file using pandas
df = pd.read_csv('eeg_data.csv')
X = df.iloc[:, :-1].values  # Get the data columns (all except the last one)
y = df.iloc[:, -1].values   # Get the label column (last one)

# Scale the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Use PCA to reduce the dimensionality of the data
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Initialize the ANN classifier with a larger maximum number of iterations
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1, max_iter=1000)

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Print the number of epochs
print(f' Number of epochs: {clf.n_iter_}') # count by iteration epochs

# Predict the labels for the test data
y_pred = clf.predict(X_test)

# Calculate the classification accuracy
accuracy = np.mean(y_pred == y_test)
print(f' Classification accuracy: {accuracy:.2f}')

# Print the classification report
print( classification_report(y_test, y_pred))


#dataset reference
from IPython.display import HTML
def display_link(url, text):
  return HTML(f'<a href="{url}" target="_blank">{text}</a>')

display_link('https://www.kaggle.com/datasets/robikscube/eye-state-classification-eeg-dataset', ' [1] Dataset EEG' '<br>'' <a href="https://chat.openai.com/chat/7142705e-56b1-4a9b-84bb-4c46b97aab47" target="_blank"> [2] Source Code</a> ')