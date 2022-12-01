import pandas as pd

def test_load():
    df = pd.read_csv('DATA/DIVOC/91-DIVOC-states-normalized.csv')
    return df