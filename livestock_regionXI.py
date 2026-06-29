import pandas as pd

livestock_price_regionXI = pd.read_csv(
    '2M4AFN10.csv',
    skiprows=2,
    sep=';',
    na_values=['..', '*/', '2/']
)

print(livestock_price_regionXI.head())

livestock_price_regionXI.rename(columns={
    'Geolocation': 'province',
    'Type': 'commodity'
}, inplace=True)

df_long = livestock_price_regionXI.melt(
    id_vars=['province', 'commodity'],
    var_name='month_year',
    value_name='price'
)

df_long['date'] = pd.to_datetime(df_long['month_year'], format='%Y %B')
df_long['province'] = df_long['province'].str.strip('.')  .str.strip()

df_long = df_long.drop(columns='month_year').sort_values(['province', 'commodity', 'date']).reset_index(drop=True)

print(df_long.head(20))
print(df_long['price'].dtypes)
print(df_long.duplicated().sum())
print(df_long['province'].unique())