import pandas as pd



def make_csv():
    for year in range(2000, 2023 + 1):
        print(year)
        df = pd.DataFrame()
        df.to_csv(f'nba_data_{year}_team.csv', index=False)
        df.to_csv(f'nba_data_{year}_opponent.csv', index=False)

if __name__ == "__main__":
    make_csv()