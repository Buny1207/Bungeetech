import pandas as pd

df = pd.read_csv (r'main.csv')

d1 = df[0:10]
Year_1960 = d1.sum(axis=0)
Year_1960['Year'] = 1960
Year_1960['Population'] = 201385000

d2 = df[10:20]
Year_1970 = d2.sum(axis=0)
Year_1970['Year'] = 1970
Year_1970['Population'] = 220099000

d3 = df[20:30]
Year_1980 = d3.sum(axis=0)
Year_1980['Year'] = 1980
Year_1980['Population'] = 248239000

d4 = df[30:40]
Year_1990 = d4.sum(axis=0)
Year_1990['Year'] = 1990
Year_1990['Population'] = 272690813

d5 = df[40:50]
Year_2000 = d5.sum(axis=0)
Year_2000['Year'] = 2000
Year_2000['Population'] = 307006550

d6 = df[50:]
Year_2001 = d6.sum(axis=0)
Year_2001['Year'] = 2010
Year_2001['Population'] = 318857056

T1 = pd.concat([Year_1960, Year_1970, Year_1980, Year_1990, Year_2000, Year_2001], axis = 1)
T1.transpose()