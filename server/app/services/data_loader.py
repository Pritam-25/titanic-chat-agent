import pandas as pd

def load_titanic_data():
    # Load the Titanic dataset from a CSV file
    df = pd.read_csv('app/data/Titanic-Dataset.csv')
    return df