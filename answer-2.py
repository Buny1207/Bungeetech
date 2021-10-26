import pandas as pd

df = pd.read_csv(r'main.csv')

dt = df[['age', 'occupation']]

occupation = list(dt['occupation'].unique())

d1 = dt.loc[df['occupation'] == 'technician']
d2 = dt.loc[df['occupation'] == 'other']
d3 = dt.loc[df['occupation'] == 'writer']
d4 = dt.loc[df['occupation'] == 'executive']
d5 = dt.loc[df['occupation'] == 'administrator']
d6 = dt.loc[df['occupation'] == 'student']
d7 = dt.loc[df['occupation'] == 'lawyer']
d8 = dt.loc[df['occupation'] == 'educator']
d9 = dt.loc[df['occupation'] == 'scientist']
d10 = dt.loc[df['occupation'] == 'entertainment']
d11 = dt.loc[df['occupation'] == 'programmer']
d12 = dt.loc[df['occupation'] == 'librarian']
d13 = dt.loc[df['occupation'] == 'homemaker']
d14 = dt.loc[df['occupation'] == 'artist']
d15 = dt.loc[df['occupation'] == 'engineer']
d16 = dt.loc[df['occupation'] == 'marketing']
d17 = dt.loc[df['occupation'] == 'none']
d18 = dt.loc[df['occupation'] == 'healthcare']
d19 = dt.loc[df['occupation'] == 'retired']
d20 = dt.loc[df['occupation'] == 'salesman']
d21 = dt.loc[df['occupation'] == 'doctor']

a_max = list((max(i['age']) for i in (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21)))
a_min = list((min(i['age']) for i in (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21)))

data = pd.DataFrame(occupation)

data.rename(columns={0: 'Occupation'}, inplace=True)

data['Min'] = a_min
data['max'] = a_max

data