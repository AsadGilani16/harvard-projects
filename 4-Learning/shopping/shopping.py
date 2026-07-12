import csv
import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    df = pd.read_csv(filename)

    months = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5, 
              'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}
    df['Month'] = df['Month'].map(months)
    
    df['VisitorType'] = (df['VisitorType'] == 'Returning_Visitor').astype(int)
    df['Weekend'] = df['Weekend'].astype(int)
    df['Revenue'] = df['Revenue'].astype(int)
    
    X = df.drop(columns=['Revenue'])
    y = df['Revenue']

    evidence = X.values.tolist()
    labels = y.to_numpy()

    return (evidence, labels)

def train_model(evidence, labels):
    # CS50 requires k=1 neighbor
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for actual, predicted in zip(labels, predictions):
        if actual == 1 and predicted == 1:
            tp += 1
        elif actual == 1 and predicted == 0:
            fn += 1
        elif actual == 0 and predicted == 1:
            fp += 1
        elif actual == 0 and predicted == 0:
            tn += 1

    # FIXED: Indentation moved outside the loop scope
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()