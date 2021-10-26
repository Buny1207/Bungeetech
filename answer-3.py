import pandas as pd

dt = pd.read_csv(r'main.csv')

dt.rename(columns={'Yellow Cards': 'Yellow_Cards', 'Red Cards': 'Red_Cards'}, inplace=True)

data = dt[['Team','Yellow_Cards','Red_Cards']]

data