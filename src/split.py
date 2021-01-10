import pandas as pd
from sklearn.model_selection import train_test_split

def split():
    df = pd.read_csv('data/interim/resale-prices-removed-duplicates.csv')
    train, test = train_test_split(df, test_size=0.2, random_state=67)
    return train, test

def main():
    train, test = split()
    train.to_csv('data/processed/resale-prices-train.csv')
    test.to_csv('data/processed/resale-prices-test.csv')

if __name__ == '__main__':
    main()