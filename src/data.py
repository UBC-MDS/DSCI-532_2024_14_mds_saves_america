import pandas as pd
import altair as alt

df = pd.read_csv("../data/processed/data_cleaned.csv")

race_ = df['race'].unique().tolist()
ideology_ = df['ideology'].unique().tolist()
higher_education_ = df['higher_education'].unique().tolist()

min_age = df['age'].min()
max_age = df['age'].max()

df_pct = df.groupby(['race', 'political_party']).size().unstack(fill_value=0).apply(
    lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')
df_pct_education = df.groupby(['higher_education', 'political_party']).size().unstack(
    fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')
