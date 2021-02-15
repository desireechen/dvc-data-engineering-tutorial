import pandas as pd

def remove_duplicates():
    df = pd.read_csv('data/raw/resale-prices.csv')
    df = df.drop_duplicates(keep="last")
    return df

def main():
    df = remove_duplicates()
    df.to_csv('data/interim/resale-prices-removed-duplicates.csv')

if __name__ == '__main__':
    main()